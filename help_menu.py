from File_import import*


class Help():
    def about(root):
        showinfo(title="Об приложении", message="Создано Войтиком Никитай")

def main(root, text, menubar):

    help = Help()

    helpMenu = Menu(menubar)
    helpMenu.add_command(label="Об приложении", command=help.about)
    menubar.add_cascade(label="Информация", menu=helpMenu)

    root.config(menu=menubar)


if __name__ == "__main__":
    print("Please run 'main.py'")