import pygame
#import linpgdev as linpg
import linpg

#对话系统
def dialog(chapterType:str, chapterId:int, screen:pygame.Surface, part:str, project_name:str=None) -> dict:
    #卸载音乐
    linpg.unloadBackgroundMusic()
    #初始化对话系统模块
    DIALOG = linpg.DialogSystem()
    if chapterType != None:
        DIALOG.new(chapterType,chapterId,part,project_name)
    else:
        DIALOG.load("Save/save.yaml")
    #DIALOG.auto_save = True
    #主循环
    while DIALOG.is_playing():
        DIALOG.draw(screen)
        linpg.display.flip()
    #返回玩家做出的选项
    return DIALOG.dialog_options

#对话编辑器
def dialogEditor(chapterType:str, chapterId:int, screen:pygame.Surface, part:str, project_name:str=None) -> None:
    #卸载音乐
    linpg.unloadBackgroundMusic()
    #加载对话
    DIALOG:object = linpg.DialogEditor(chapterType,chapterId,part,project_name)
    #主循环
    while DIALOG.is_playing():
        DIALOG.draw(screen)
        linpg.display.flip()

class MainMenu(linpg.SystemWithBackgroundMusic):
    def __init__(self,screen):
        #初始化系统模块
        linpg.SystemWithBackgroundMusic.__init__(self)
        self.set_bgm("Assets/music/main_menu_bgm.ogg")
        #窗口标题图标
        linpg.display.set_icon("Assets/image/UI/icon.png")
        linpg.display.set_caption(linpg.get_lang('GameTitle'))
        #加载主菜单背景
        self.bg_img = linpg.loadImage("Assets/image/UI/bg0.png",(0,0),screen.get_width(),screen.get_height())
        #初始化返回菜单判定参数
        linpg.set_glob_value("BackToMainMenu",False)
        self.set_bgm_volume(linpg.get_setting("Sound","background_music")/100)
    def draw(self, screen):
        self._update_event()
        self.play_bgm()
        #背景视频
        self.bg_img.draw(screen)
        for event in self.events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                dialog("main_chapter",1,screen,"dialog_example")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                dialogEditor("main_chapter",1,screen)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.stop()

#是否启动游戏
GAMESTART:bool = True

#游戏主进程
if GAMESTART is True and __name__ == "__main__":
    #创建窗口
    screen = linpg.display.init_screen(
        pygame.DOUBLEBUF | pygame.SCALED | pygame.FULLSCREEN if linpg.get_setting("FullScreen") is True else pygame.SCALED
        )
    #主菜单模块
    mainMenu = MainMenu(screen)
    #主循环
    while mainMenu.is_playing():
        mainMenu.draw(screen)
        linpg.display.flip()
    #释放内容占用
    linpg.display.quit()
