# with open("Day24/my_file.txt") as file:
#     content = file.read()
#     print(content)
# with open("Day24/my_file.txt",mode="a") as file: # w delete previously content a protects old one
#     file.write("\nNew content")

# to Create new file use w
# with open("Day24/new_file.txt",mode="w")as new_file:
#     new_file.write("This is my new file")

# f= open("Day24/my_file.txt","r")
# firts_line= f.readlines()[0]
# update_name= firts_line.replace("New content", "[name]")
# print(firts_line)


def create_mail_text(directory, name):
    with open(directory, "r") as file:
        whole_text = file.read().replace("[name]", name)
       
        with open(f"Day24/Maillist/{name}.txt", "w") as file:
            file.write(whole_text)


def create_mails(invitations):
    for name in invitations:
        create_mail_text("Day24/my_file.txt", name)


def get_invitations():
    with open("Day24/Invitations/invitations.txt", "r") as file:
        content = file.readlines()
        trimmed_content = []
        for c in content:
            trimmed_content.append(c.strip())
        return trimmed_content


create_mails(get_invitations())
