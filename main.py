# import linpg game engine 导入linpg引擎
import linpg

# initialize the window 初始化窗口
linpg.display.init()


# dialog system 对话系统
def dialog(chapterType: str, chapterId: int, part: str) -> None:
    # unload main menu's background music 卸载主菜单的音乐
    linpg.media.unload()
    # initialize dialog module 初始化对话系统模块
    DIALOG: linpg.VisualNovelPlayer = linpg.VisualNovelPlayer()
    DIALOG.new(chapterType, chapterId, part)
    # DIALOG.auto_save = True
    # main loop 主循环
    while DIALOG.is_playing():
        DIALOG.draw_on_screen()
        linpg.display.flip()


# dialog editor system 对话编辑器
def dialogEditor(chapterType: str, chapterId: int, part: str) -> None:
    # unload main menu's background music 卸载主菜单的音乐
    linpg.media.unload()
    # initialize editor module 加载编辑器
    DIALOG: linpg.VisualNovelEditor = linpg.VisualNovelEditor()
    DIALOG.new(chapterType, chapterId, part)
    # main loop 主循环
    while DIALOG.is_playing():
        DIALOG.draw_on_screen()
        linpg.display.flip()


# 主菜单
class MainMenu(linpg.SystemWithBackgroundMusic):
    # a panel that will show info of developer 开发者信息面板
    __developer_info_panel: linpg.GameObjectsDictContainer = (
        linpg.ui.generate_container("developer_info")
    )
    # a button that will open dialog editor 打开对话编辑器的按钮
    __show_dialog_editor_button: linpg.Button = linpg.load.button(
        r"Assets/image/ui/edit.png",
        (int(linpg.display.get_width() * 0.85), int(linpg.display.get_height() * 0.05)),
        (
            int(linpg.display.get_height() * 0.06),
            int(linpg.display.get_height() * 0.05),
        ),
        200,
    )
    # a button that will show developer info panel when it is clicked 开发者信息按钮
    __show_developer_info_button: linpg.Button = linpg.load.button(
        r"Assets/image/ui/important.png",
        (int(linpg.display.get_width() * 0.9), int(linpg.display.get_height() * 0.05)),
        (
            int(linpg.display.get_height() * 0.05),
            int(linpg.display.get_height() * 0.05),
        ),
        200,
    )
    # a button that will show exit confirm panel when it is clicked 退出按钮
    __exit_button: linpg.Button = linpg.load.button(
        r"Assets/image/ui/quit.png",
        (int(linpg.display.get_width() * 0.95), int(linpg.display.get_height() * 0.05)),
        (
            int(linpg.display.get_height() * 0.05),
            int(linpg.display.get_height() * 0.05),
        ),
        200,
    )
    # Main menu's background image 主菜单背景
    __BACKGROUND_IMAGE: linpg.StaticImage = linpg.load.static_image(
        r"Assets/image/ui/bg0.png", (0, 0), linpg.display.get_size()
    )

    def __init__(self) -> None:
        # initialize primary module 初始化系统模块
        super().__init__()
        # setup main menu's background music 设置背景音乐
        self.set_bgm(r"Assets/music/main_menu_bgm.ogg")
        self.set_bgm_volume(linpg.volume.get_background_music() / 100)

    def draw(self, _surface: linpg.ImageSurface) -> None:
        # ensure the background music is play 确认背景音乐在播放
        self.play_bgm()
        # draw the background image onto the screen 画出背景图片
        self.__BACKGROUND_IMAGE.draw(_surface)
        # handling input events 处理输入
        if linpg.controller.get_event("confirm"):
            if self.__developer_info_panel.is_visible():
                if self.__developer_info_panel.item_being_hovered == "notice":
                    self.__developer_info_panel.set_visible(False)
            elif self.__show_dialog_editor_button.is_hovered():
                dialogEditor("main_chapter", 1, "dialog_example")
                self.set_bgm_volume(linpg.volume.get_background_music() / 100)
            elif self.__show_developer_info_button.is_hovered():
                self.__developer_info_panel.set_visible(True)
            elif self.__exit_button.is_hovered():
                # make sure user wants to quit
                if linpg.ConfirmationDialogBox(
                    linpg.lang.get_text("Global", "tip"),
                    linpg.lang.get_text("LeavingWithoutSavingWarning", "exit_confirm"),
                ).show():
                    self.stop()
            else:
                dialog("main_chapter", 1, "dialog_example")
                self.set_bgm_volume(linpg.volume.get_background_music() / 100)
        # draw the ui (if they are visible) 画出ui
        self.__show_dialog_editor_button.draw(_surface)
        self.__show_developer_info_button.draw(_surface)
        self.__developer_info_panel.draw(_surface)
        self.__exit_button.draw(_surface)


# a tag that is used to control whether to start the game 是否启动游戏
GAME_START: bool = True

# main function 游戏主进程
if GAME_START is True and __name__ == "__main__":
    # set icon 窗口图标
    linpg.display.set_icon(r"Assets/image/ui/icon.png")
    # set title 窗口标题
    linpg.display.set_caption("A Story of Us")
    # initialize main module 主菜单模块
    mainMenu: MainMenu = MainMenu()
    # compile all the dialogue scripts in Data directory 编译Data文件夹内的所有原始视觉小说脚本文件
    linpg.ScriptCompiler.compile("Data")
    # main loop 主循环
    while mainMenu.is_playing():
        mainMenu.draw_on_screen()
        linpg.display.flip()
