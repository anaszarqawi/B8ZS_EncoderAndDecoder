from pypresence import Presence
import time


class data():
    stateV, detailsV, imageV, captionV, tokenV, button, label, url = "", "", "", "", "", "", "", ""

    def Custom(self, s, d, i, c, t):
        self.state = s
        self.details = d
        self.image = i
        self.caption = c
        self.token = t

    def Custom_With_Btn(self, s, d, i, c, t, l, u):
        self.state = s
        self.details = d
        self.image = i
        self.caption = c
        self.token = t
        self.label = l
        self.url = u

    def Rts(self):
        self.state = "In RTS Workspace"
        self.details = "Editing"
        self.image = "rts"
        self.caption = "Road To Success"
        self.label = "RTS WORKSPACE"
        self.url = "https://bit.ly/RTSworksapace"
        self.token = "839175397685723216"

    def Asphalt(self):
        self.state = "In Racing"
        self.details = "Playing"
        self.image = "asphalt"
        self.caption = "Asphalt 9 : Legends"
        self.token = "922213462531276860"


app = data()


def GetChoice():
    global stateV, detailsV, imageV, captionV, tokenV, button, label, url

    stateV = input("Enter The State : ")
    detailsV = input("Enter The Details : ")
    imageV = input("Enter The Image Name : ")
    captionV = input("Enter The Caption For Image : ")
    tokenV = input("Enter The Token : ")

    c = input("Do you want to add buttons ? (y,n) : ")

    if(c == 'y'):
        label = input("Enter The Label : ")
        url = input("Enter URL : ")

    return c


def connect(data, btn="y"):
    rpc = Presence(app.token)
    rpc.connect()

    if btn == "y":
        rpc.update(state=app.state,
                   details=app.details,
                   large_image=app.image,
                   large_text=app.caption,
                   buttons=[{"label": app.label,
                             "url": app.url
                             }],
                   start=time.time())
    else:
        rpc.update(state=app.state,
                   details=app.details,
                   large_image=app.image,
                   large_text=app.caption,
                   start=time.time())

    status = print("Rich presence is running perfectly fine!")

    while True:
        c = input("c : change\n"
                  "q : close\n"
                  "------------\n")
        if close == "q":
            rpc.close()
            break
        elif c == "c":
            run()


def run():
    choice = int(input("1- RTS\n2- Asphalt\n3- Custom\n----------\n"))

    if (choice == 1):
        app.Rts()
        connect(app)
    elif (choice == 2):
        app.Asphalt()
        connect(app)
    elif (choice == 3):
        btn = GetChoice()

        if btn == "y":
            app.Custom_With_Btn(stateV, detailsV, imageV,
                                captionV, tokenV, label, url)
        else:
            app.Custom(stateV, detailsV, imageV, captionV, tokenV)
        connect(app, btn)


run()
