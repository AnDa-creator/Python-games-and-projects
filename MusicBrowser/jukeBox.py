import sqlite3
import tkinter

conn = sqlite3.connect('music.sqlite',)


class Scrollbox(tkinter.Listbox):

    def __init__(self, window, **kwargs):
        # tkinter.Listbox.__init__(self, window, **kwargs) #python 2
        super().__init__(window, **kwargs)

        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky="nsw", rowspan=1, columnspan=1, **kwargs):
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


class DataListBox(Scrollbox):

    def __init__(self, window,connection,table, field, sort_order=(), **kwargs):

        super().__init__(window, **kwargs)

        self.linked_box = None
        self.link_field = None
        self.traceback = None

        self.cursor = connection.cursor()
        self.table = table
        self.field = field

        self.bind('<<ListboxSelect>>', self.on_select)

        self.sql_select = "SELECT " + self.field + ", _id" + " FROM " + self.table
        if sort_order:
            self.sql_sort = " ORDER BY " + ','.join(sort_order)
        else:
            self.sql_sort = " ORDER BY " + self.field

    def clear(self):
        self.delete(0, tkinter.END)

    def link(self, widget, link_field):
        self.linked_box = widget
        widget.link_field = link_field

    def requery(self, link_value=None):
        if link_value and self.link_field:
            sql = self.sql_select + " WHERE " + self.link_field + " =?" + self.sql_sort
            # print(sql) # TODO delete this line
            self.cursor.execute(sql, (link_value,))
            self.traceback = link_value,self.table
        else:
            # print(self.sql_select + self.sql_sort) # TODO delete this line
            self.cursor.execute(self.sql_select + self.sql_sort)

        # clear the listbox contents before re-loading
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[0])

        if self.linked_box:
            self.linked_box.clear()

    def on_select(self, event):
        if self.linked_box:
            print(self is event.widget) #TODO delete this line
            lb = event.widget
            try:
                index = int(lb.curselection()[0])
            except IndexError:
                pass
            value = lb.get(index),
            count = self.cursor.execute("SELECT " + "count(" + self.field +")" + ", _id" + " FROM " + self.table +
                                        " WHERE " + self.field + "=?", value).fetchone()[0]
            if count == 1:
                link_id = self.cursor.execute(self.sql_select + " WHERE " + self.field + "=?", value).fetchone()[1]
                text = self.sql_select + " WHERE " + self.field + "=?"
                print(text)
            else:
                text = self.sql_select + " WHERE " + self.field + "=?" + " AND " + self.traceback[1] + ".artist" + "=" \
                       + str(self.traceback[0])
                print(text)
                link_id = self.cursor.execute(text, value).fetchone()[1]
            print(link_id)
            self.linked_box.requery(link_id)
    # get the artist ID from the database row
        # artist_id = conn.execute("SELECT artists._id FROM artists WHERE artists.name=?", artist_name).fetchone()
        # alist = []
        # for row in conn.execute("SELECT albums.name FROM albums WHERE albums.artist = ? ORDER BY albums.name", artist_id):
        #     alist.append(row[0])
        # albumLV.set(tuple(alist))
        # songLV.set(("Choose an album",))


# def get_songs(event):
#     lb = event.widget
#     index = int(lb.curselection()[0])
#     album_name = lb.get(index),
#     album_id = conn.execute("SELECT albums._id FROM albums WHERE albums.name=?", album_name).fetchone()
#
#     # get the artist ID from the database row
#     album_id = conn.execute("SELECT albums._id FROM albums WHERE albums.name=?", album_name).fetchone()
#     alist = []
#     for x in conn.execute("SELECT songs.title FROM songs WHERE songs.album=? ORDER BY songs.track", album_id):
#         alist.append(x[0])
#     songLV.set(tuple(alist))
if __name__ == '__main__':


    mainwindow = tkinter.Tk()
    mainwindow.title('Music DB Browser')
    mainwindow.geometry('1024x768')

    mainwindow.columnconfigure(0, weight=2)
    mainwindow.columnconfigure(1, weight=2)
    mainwindow.columnconfigure(2, weight=2)
    mainwindow.columnconfigure(3, weight=1) # spacer column on right

    mainwindow.rowconfigure(0, weight=1)
    mainwindow.rowconfigure(1, weight=5)
    mainwindow.rowconfigure(2, weight=5)
    mainwindow.rowconfigure(3, weight=1)

    # ======== labels =========
    tkinter.Label(mainwindow, text="Artists").grid(row=0, column=0)
    tkinter.Label(mainwindow, text="Albums").grid(row=0, column=1)
    tkinter.Label(mainwindow, text="Songs").grid(row=0, column=2)

    # ======== Artists listbox ========
    artistList = DataListBox(mainwindow, conn, "artists", "name")
    artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30,0))
    artistList.config(border=2, relief='sunken')

    for artist in conn.execute("SELECT artists.name FROM artists ORDER BY artists.name"):
        artistList.insert(tkinter.END, artist[0])

    artistList.requery()

    # ===== Album Listbox ======
    albumLV = tkinter.Variable(mainwindow)
    albumLV.set(("Choose an artist",))
    albumList = DataListBox(mainwindow, conn, "albums","name", sort_order=("name",))
    albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
    albumList.config(border=2, relief='sunken')

    # albumList.bind('<<ListboxSelect>>', get_songs)
    artistList.link(albumList, "artist")
    # ===== Songs Listbox =====
    songLV = tkinter.Variable(mainwindow)
    songLV.set(("Choose an album",))
    songList = DataListBox(mainwindow, conn, "songs", "title", ('track', 'title'))

    songList.grid(row=1, column=2, sticky='nsew', padx=(30,0))
    songList.config(border=2, relief='sunken')

    albumList.link(songList, "album")
    # artistScroll = tkinter.Scrollbar(mainwindow, orient=tkinter.VERTICAL, command=artistList.yview)
    # artistScroll.grid(row=1, column=0, sticky='nse', rowspan=2)
    # artistList["yscrollcommand"] = artistList

    # ===== Main Loop =====
    mainwindow.mainloop()
    print("Closing database connection")
    conn.close()
