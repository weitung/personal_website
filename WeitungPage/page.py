import sys, os
import Famcy
import json
from WeitungPage.wstyle import *
from WeitungPage.section_title import *
from gadgethiServerUtils.file_basics import *

abs_path = os.path.abspath(__file__)
abs_path = abs_path.replace("page.py", "_projects")

project_files = Famcy.FManager.listdir_exclude(abs_path, "", exclude_list=[".", "_"])
project_dict = {}

for f in project_files:
    value = read_config_yaml(abs_path+"/"+f)
    key = f.replace(".yaml", "")
    project_dict[key] = value
    with open(abs_path+"/_content/"+key+".md") as ff:
        project_dict[key].update({
            "content": ff.read()
            })

# Define the order of default project
key_list = list(project_dict.keys())
key_list.sort()

class WeitungPage(Famcy.FamcyPage):
    def __init__(self):
        super(WeitungPage, self).__init__("/", WeitungPersonalPageStyle(), background_thread=False)
        
        self.table_info = []

        self.project_card = self.project()
        self.card_1 = self.card1()
        self.layout.addWidget(self.card_1, 0, 0)
        self.layout.addWidget(self.project_card, 1, 0)

    def card1(self):
        card1 = Famcy.FamcyCard()
        card1.body["style"] = "height: 100vh; justify-content: center;"
        inner_card = Famcy.FamcyCard()
        profile_pic = Famcy.displayPicWord()
        profile_pic.update({
                "title": "",
                "content": "",
                "img_src": "/asset/image/weitung.jpeg"
            })

        btn_to_project = Famcy.urlBtn()
        btn_to_project.update({
            "button_name": "Projects",
            "url": "#"+self.project_card.id
            })

        btn_to_cv = Famcy.urlBtn()
        btn_to_cv.update({
            "button_name": "CV",
            "url": "/asset/docs/cv.pdf"
            })
        

        about_me = Famcy.displayParagraph()
        about_me.update({
                "title": "FAMCY",
                "content": "cotent contentcotent contentcotent contentcotent contentcotent contentcotent contentcotent content"
            })

        inner_card.layout.addWidget(about_me, 0, 0, 1, 2)
        inner_card.layout.addWidget(btn_to_project, 1, 0, 1, 1)
        inner_card.layout.addWidget(btn_to_cv, 1, 1, 1, 1)

        card1.layout.addWidget(profile_pic, 0, 0)
        card1.layout.addWidget(inner_card, 0, 1)

        return card1

    def project(self):
        card2 = Famcy.FamcyCard()
        ilist = Famcy.inputList()
        sbtn = Famcy.submitBtn()
        filtering = Famcy.FamcyCard()
        filtering.layout.addWidget(ilist,0,0)
        filtering.layout.addWidget(sbtn,0,1)

        title = sectionTitle()
        title.update({
            "title": "Selected Projects"
            })
        title.body["style"] = "text-align:center;"
        dummy = Famcy.FamcyCard()
        card2.layout.addWidget(title, 0, 0, 1, 3)
        card2.layout.addWidget(filtering, 1,2, 1, 1)
        card2.layout.addWidget(dummy, 1,0, 1, 2)

        for j in range((len(key_list) + 2)// 3):
            for i in range(3):
                k = key_list[j*3+i]
                profile_pic = Famcy.displayPicWord()
                profile_pic.update({
                        "title": project_dict[k]["title"],
                        "content": project_dict[k]["short_desc"],
                        "img_src": project_dict[k]["img_url"]
                    })

                profile_pic.body["onclick"] = "location.href='/%s';" % k

                card2.layout.addWidget(profile_pic, j+2,i, 1, 1)

        return card2

class ProjectPage(Famcy.FamcyPage):
    def __init__(self, pid):
        super(ProjectPage, self).__init__("/"+pid, WeitungPersonalPageStyle(), background_thread=False)

        content = Famcy.displayParagraph()
        content.update({
            "title": "", 
            "content": project_dict[pid]["content"]
            })

        self.layout.addWidget(content, 0, 0)

for k in key_list:
    p = ProjectPage(k)
    p.register()

page = WeitungPage()
page.register()



