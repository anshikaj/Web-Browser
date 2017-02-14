import gtk , webkit 

def go_but(widget):
	add = addressbar.get_text()
	if add.startswith("http://"):
		web.open(add)
	else:
	     add = "http://" + add
	     addressbar.set_text(add )
	     web.open(add )

win = gtk.Window()
win.connect('destroy',lambda w: gtk.main_quit())

box1 = gtk.VBox()
win.add(box1)

box2 = gtk.HBox()
box1.pack_start(box2, False)

addressbar = gtk.Entry()
box2.pack_start(addressbar)

gobutton = gtk.Button("GO")
box2.pack_start(gobutton)
gobutton.connect('clicked' , go_but)
scroller = gtk.ScrolledWindow()
box1.pack_start(scroller)

web = webkit.WebView()
scroller.add(web)
win.show_all()
gtk.main()