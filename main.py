# 导入linpg引擎
try:
    import linpgdev as linpg
except Exception:
    import linpg

# 对话系统
def dialog(
    chapterType: str, chapterId: int, part: str, projectName: str = None
) -> None:
    # 卸载音乐
    linpg.media.unload()
    # 初始化对话系统模块
    DIALOG: linpg.DialogSystem = linpg.DialogSystem()
    if chapterType is None:
        DIALOG.load(r"Save/save.yaml")
    else:
        DIALOG.new(chapterType, chapterId, part, projectName)
    # DIALOG.auto_save = True
    # 主循环
    while DIALOG.is_playing():
        DIALOG.draw_on_screen()
        linpg.display.flip()


# 对话编辑器
def dialogEditor(
    chapterType: str, chapterId: int, part: str, projectName: str = None
) -> None:
    # 卸载音乐
    linpg.media.unload()
    # 加载对话
    DIALOG: linpg.DialogEditor = linpg.DialogEditor()
    DIALOG.load(chapterType, chapterId, part, projectName)
    # 主循环
    while DIALOG.is_playing():
        DIALOG.draw_on_screen()
        linpg.display.flip()


# 主菜单
class MainMenu(linpg.SystemWithBackgroundMusic):
    def __init__(self):
        # 初始化系统模块
        super().__init__()
        # 加载主菜单背景
        self.bg_img = linpg.load.static_image(
            r"Assets/image/UI/bg0.png", (0, 0), linpg.display.get_size()
        )
        # 初始化返回菜单判定参数
        linpg.global_value.set("BackToMainMenu", False)
        # 设置背景音乐
        self.set_bgm(r"Assets/music/main_menu_bgm.ogg")
        self.set_bgm_volume(linpg.media.volume.background_music / 100)
        # 开发者信息
        self.show_developer_info_button = linpg.load.button(
            r"Assets/image/UI/important.png",
            (linpg.display.get_width() * 0.9, linpg.display.get_height() * 0.05),
            (linpg.display.get_height() * 0.05, linpg.display.get_height() * 0.05),
            200,
        )
        self.developer_info = linpg.ui.generate(
            linpg.config.load(r"Data/ui.yaml", "developer_info")
        )
        self.exit_button = linpg.load.button(
            r"Assets/image/UI/quit.png",
            (linpg.display.get_width() * 0.95, linpg.display.get_height() * 0.05),
            (linpg.display.get_height() * 0.05, linpg.display.get_height() * 0.05),
            200,
        )
        main_menu_txt = linpg.lang.get_text("MainMenu")
        self.exit_confirm_menu = linpg.Message(
            main_menu_txt["other"]["tip"],
            main_menu_txt["other"]["exit_confirm"],
            (main_menu_txt["other"]["confirm"], main_menu_txt["other"]["deny"]),
            True,
            return_button=1,
            escape_button=1,
        )

    def draw_on_screen(self) -> None:
        # 确认背景音乐在播放
        self.play_bgm()
        # 画出背景图片
        self.bg_img.draw_on_screen()
        # 处理输入
        for event in linpg.controller.events:
            if event.type == linpg.MOUSE_BUTTON_DOWN and event.button == 1:
                if not self.developer_info.hidden:
                    if self.developer_info.item_being_hovered == "notice":
                        self.developer_info.hidden = True
                elif (
                    self.developer_info.hidden is True
                    and self.show_developer_info_button.is_hover()
                ):
                    self.developer_info.hidden = False
                elif linpg.is_hover(self.exit_button):
                    if self.exit_confirm_menu.show() == 0:
                        self.stop()
                else:
                    dialog("main_chapter", 1, "dialog_example")
                    self.set_bgm_volume(linpg.media.volume.background_music / 100)
            elif event.type == linpg.key.DOWN and event.unicode == "p":
                dialogEditor("main_chapter", 1, "dialog_example")
                self.set_bgm_volume(linpg.media.volume.background_music / 100)
        # 画出ui
        self.show_developer_info_button.draw_on_screen()
        self.developer_info.draw_on_screen()
        self.exit_button.draw_on_screen()


# 是否启动游戏
GAMESTART: bool = True

# 游戏主进程
if GAMESTART is True and __name__ == "__main__":
    # 创建窗口
    linpg.display.init()
    # 窗口标题图标
    linpg.display.set_icon(r"Assets/image/UI/icon.png")
    linpg.display.set_caption(linpg.lang.get_text("GameTitle"))
    # 主菜单模块
    mainMenu = MainMenu()
    # 主循环
    while mainMenu.is_playing():
        mainMenu.draw_on_screen()
        linpg.display.flip()

# 释放内容占用
linpg.display.quit()
