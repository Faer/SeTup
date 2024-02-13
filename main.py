import webbrowser as w
import sys
import smtplib
import pygame

version = "0.8_03F"

open_version = "12.02.2024"
avtor = "Fa_r gre_si (Никнейм)"

"""
https://t.me/+pp2_OmUdWmJhZDFi
"""

color_color = ()
app_color = (210,185,15)
dosk_color = (100,100,100)
dosk_color_ = (60,60,60)
menu_color = (225,225,225)
menu_color_ = (25,0,0)
screen_color = (235,235,235)
txt_color = (190,190,190)
txt_color_30 = (30,30,30)
txt_color_60 = (60,60,60)
txt_color_90 = (90,90,90)
txt_color_140 = (140,140,140)
info_dosk_color = (190,190,190)
info_dosk2_color = (110,110,110)
exit_panel_color = (180,180,180)
exit_panel_color_ = (120,120,120)
opj_color = ()
button_color = ()

button_color_90 = (90,90,90)
button_color_140 = (140,140,140)

pygame.init()
screen = pygame.display.set_mode()

button = pygame.Surface((200 ,150))
button.fill((255,150,10))

app = pygame.Surface((1080 ,210))

menu = pygame.Surface((115,20))
menu.fill((menu_color))
menu_ = pygame.Surface((181,171))
menu_.fill((menu_color_))

dosk = pygame.Surface((600,2030))
dosk.fill((dosk_color))
dosk_ = pygame.Surface((580,1990))
dosk_.fill((dosk_color_))
dosk_exit = pygame.Surface((600,2030))
dosk_exit.fill((90,90,90))

info_dosk_button = pygame.Surface((430,150))
info_dosk_button.fill((95,97,95))
info_dosk_button_ = pygame.Surface((410,130))
info_dosk_button_.fill((40,40,40))

setup_button = pygame.Surface((430,150))
setup_button.fill((95,97,95))
setup_button_ = pygame.Surface((410,130))
setup_button_.fill((40,40,40))

home_button = pygame.Surface((430,150))
home_button.fill((95,97,95))
home_button_ = pygame.Surface((410,130))
home_button_.fill((40,40,40))

setting_button = pygame.Surface((430,150))
setting_button.fill((95,97,95))
setting_button_ = pygame.Surface((410,130))
setting_button_.fill((40,40,40))

exit_button = pygame.Surface((430,150))
exit_button.fill((95,97,95))
exit_button_ = pygame.Surface((410,130))
exit_button_.fill((40,40,40))

secret_button = pygame.Surface((430,150))
secret_button.fill((95,97,95))
secret_button_ = pygame.Surface((410,130))
secret_button_.fill((40,40,40))

secret_divan = pygame.Surface((300,300))
secret_divan.fill((40,40,40))
secret_divan_ = pygame.Surface((280,280))
secret_divan_.fill((95,97,95))

dosk2_txt = pygame.Surface((470,230))
dosk2_txt.fill((95,97,95))
dosk3_txt = pygame.Surface((450,210))
dosk3_txt.fill((40,40,40))

setup_calc = pygame.Surface((330,410))
setup_calc.fill((170,120,0))
setup_calc_ = pygame.Surface((310,310))
setup_calc_.fill((200,140,10))

setup_setupyt = pygame.Surface((330,410))
setup_setupyt.fill((170,120,0))
setup_setupyt_ = pygame.Surface((310,310))
setup_setupyt_.fill((200,140,10))

info_button = pygame.Surface((140,140))
info_button_ = pygame.Surface((170,120))
mail_button = pygame.Surface((725,100))

yes_button_ = pygame.Surface((230,130))
yes_button = pygame.Surface((210,110))
no_button_ = pygame.Surface((230,130))
no_button = pygame.Surface((210,110))

info_dosk = pygame.Surface((1025,1150))
info_dosk2 = pygame.Surface((1055,1180))
copy_png_ = pygame.Surface((70,70))

exit_panel = pygame.Surface((880,410))
exit_panel.fill((180,180,180))
exit_panel_ = pygame.Surface((900,430))
exit_panel_.fill((110,110,110))

num_button = pygame.Surface((155,155))
num_button.fill((120,120,120))

one_num = pygame.Surface((175,175))
one_num.fill((180,180,180))

two_num = pygame.Surface((175,175))
two_num.fill((180,180,180))

tree_num = pygame.Surface((175,175))
tree_num.fill((180,180,180))

four_num = pygame.Surface((175,175))
four_num.fill((180,180,180))

five_num = pygame.Surface((175,175))
five_num.fill((180,180,180))

six_num = pygame.Surface((175,175))
six_num.fill((180,180,180))

seven_num = pygame.Surface((175,175))
seven_num.fill((180,180,180))

eight_num = pygame.Surface((175,175))
eight_num.fill((180,180,180))

nine_num = pygame.Surface((175,175))
nine_num.fill((180,180,180))

zero_num = pygame.Surface((175,175))
zero_num.fill((180,180,180))

delet_num = pygame.Surface((175,175))
delet_num.fill((180,180,180))

enter_num = pygame.Surface((175,175))
enter_num.fill((180,180,180))

panel_num = pygame.Surface((630,155))
panel_num.fill((180,180,180))
panel_num_ = pygame.Surface((610,135))
panel_num_.fill((120,120,120))

setting_color = pygame.Surface((175,175))
setting_color.fill((180,180,180))

mouse_button = pygame.Surface((40,40))

txt = pygame.font.Font(None, 80)
txt_ = pygame.font.Font(None, 110)
txt__ = pygame.font.Font(None, 140)
txt___ = pygame.font.Font(None, 170)

calc_txt = txt.render("Calc.py", False,  (240,240,240))
setupyt_txt = txt.render("!??????!", False,  (240,240,240))

one_txt = txt___.render("1", False,  (txt_color))
two_txt = txt___.render("2", False,  (txt_color))
tree_txt = txt___.render("3", False,  (txt_color))
four_txt = txt___.render("4", False,  (txt_color))
five_txt = txt___.render("5", False,  (txt_color))
six_txt = txt___.render("6", False,  (txt_color))
seven_txt = txt___.render("7", False,  (txt_color))
eight_txt = txt___.render("8", False,  (txt_color))
nine_txt = txt___.render("9", False,  (txt_color))
zero_txt = txt___.render("0", False,  (txt_color))

info_dosk_txt = txt.render("INFO", False,  (txt_color))
setting_txt = txt.render("Setting", False,  (txt_color))
exit_txt = txt.render("Exit", False,  (txt_color))
setup_txt = txt.render("Setup", False,  (txt_color))
home_txt = txt.render("home", False,  (txt_color))
secret_txt = txt.render("Secret", False,  (txt_color))
dosk_txt = txt_.render("Выберите", False,  (50,125,200))
dosk1_txt = txt_.render("Категорию", False,  (50,125,200))
info_txt = txt_.render("i", False,  (200,200,200))

none_txt = txt___.render("Пусто", False,  (txt_color_60))

enter_txt = txt.render("Entr", False,  (60,60,60))
txt__txt = txt_.render("_", False,  (200,200,200))

info6_txt = txt.render("Дата создании: 23.01.2024", False,  (60,160,60))

calc_png= pygame.image.load('Calc.png')
setupyt_png= pygame.image.load('Calc.png')
copy_png= pygame.image.load('Copy.png')

running = True
setup = False
x_dosk = 550
stop_setup = 0
dosk_proverca = False
dosk_right = False
dosk_left = False
exit_dosk = -50
home = "home"
run = True
act_dosk = False
dosk_act = False
info_dosk_ = False
home_copy = None
info_exit = 1000
info_exit_ = 0
one_point = 1
one_point_ = 1
panel = ""
password = ""
user = ""
password_len = 0
mouse_act = False
mouse_stop = False

while running:
	
	app.fill((app_color))
	info_dosk.fill((info_dosk_color))
	info_dosk2.fill((info_dosk2_color))
	exit_panel.fill((info_dosk_color))
	exit_panel_.fill((info_dosk2_color))
	
	no_button.fill((button_color_140))
	yes_button.fill((button_color_140))
	no_button_.fill((button_color_90))
	yes_button_.fill((button_color_90))
	
	info_exit_txt = txt_.render("<---", False,  (txt_color_60))
	home1_1_txt = txt_.render("Вас приветствует SePyt", False,  (txt_color_30))
	home1_2_txt = txt.render("Спасибо что используете нас!", False,  (txt_color_30))
	home2_1_txt = txt.render("Научите меня пожалуйста компили-", False,  (txt_color_30))
	home2_2_txt = txt.render("ровать '.py' в apk и windosws 32-bit!", False,  (txt_color_30))
	home2_3_txt = txt.render("(Почта есть в ИНФО)", False,  (txt_color_30))
	
	setupy_txt = txt.render("Файлы с '.py ' нужно приложение", False,  (txt_color_30))
	setupy1_txt = txt.render("котороый умеет читать PYTHON", False,  (txt_color_30))
	
	info1_txt = txt.render("Владелц: " + str(avtor), False,  (txt_color_60))

	info2_txt = txt.render("Версия: " + str(version), False,  (txt_color_60))
	
	yes_txt = txt_.render("Да", False,  (txt_color_30))
	no_txt = txt_.render("Нет", False,  (txt_color_30))
	
	info3_1_txt = txt.render("Это приложение создано для ска-", False,  (txt_color_60))
	info3_2_txt = txt.render("чивания моих приложени и игр, он", False,  (txt_color_60))
	info3_3_txt = txt.render("был как моим первым приложени-", False,  (txt_color_60))
	info3_4_txt = txt.render("ем а не игра, Хочу сказать спасибо", False,  (txt_color_60))
	info3_5_txt = txt.render("что используете моё приложение!", False,  (txt_color_60))
	info5_txt = txt.render("Последние обнавление: " + str(open_version), False,  (60,160,60))
	exit_exit_txt = txt_.render("Вы уверены", False,  (txt_color_60))
	exit_exit1_txt = txt_.render("что хотите выйти?", False,  (txt_color_60))
	
	info4_1_txt = txt.render("Почта: ", False,  (txt_color_60))
	info4_2_txt = txt.render("Stalkerzxcret@gmail.com", False,  (0,80,250))
		
	mouse = pygame.mouse.get_pos()
		
	screen.fill((screen_color))
	screen.blit(app,(550-x_dosk, 0))
	
	"""
	screen.blit(menu_,(568-x_dosk, 30))
	"""
	
	screen.blit(menu,(600-x_dosk, 65))
	screen.blit(menu,(600-x_dosk, 105))
	screen.blit(menu,(600-x_dosk, 145))
	
	screen.blit(dosk,(-50 - x_dosk, 0))
	screen.blit(dosk_,(-50 - x_dosk, 20))
	
	screen.blit(setup_button,(35 - x_dosk, 500))
	screen.blit(setup_button_,(45 - x_dosk, 510))
	
	screen.blit(exit_button,(35 - x_dosk, 1800))
	screen.blit(exit_button_,(45 - x_dosk, 1810))
	
	screen.blit(setting_button,(35 - x_dosk, 1400))
	screen.blit(setting_button_,(45 - x_dosk, 1410))
	
	screen.blit(secret_button,(35 - x_dosk, 1200))
	screen.blit(secret_button_,(45 - x_dosk, 1210))

	screen.blit(info_dosk_button,(35 - x_dosk, 1600))		
	screen.blit(info_dosk_button_,(45 - x_dosk, 1610))
	
	screen.blit(home_button,(35 - x_dosk, 310))
	screen.blit(home_button_,(45 - x_dosk, 320))
	
	screen.blit(dosk2_txt,(18 - x_dosk, 40))
	screen.blit(dosk3_txt,(28 - x_dosk, 50))
	
	screen.blit(dosk_txt,(60 - x_dosk, 65))
	screen.blit(dosk1_txt,(45 - x_dosk, 175))
	
	screen.blit(setup_txt,(160 - x_dosk, 545))
	screen.blit(home_txt,(165 - x_dosk, 360))
	screen.blit(setting_txt,(145 - x_dosk, 1450))
	screen.blit(secret_txt,(160 - x_dosk, 1250))
	screen.blit(info_dosk_txt,(175-x_dosk, 1650))
	screen.blit(exit_txt,(185 - x_dosk, 1850))
		
	if not home == "exit":
		pygame.draw.circle(screen, (10,90,190), (1540 - x_dosk,114), 50, 250)
		pygame.draw.circle(screen, (210,210,210), (1540 - x_dosk,114), 55, 7)
		
		screen.blit(info_txt,(1529-x_dosk,83))
		
		info_rect = info_button.get_rect(topleft=(1470- x_dosk,45))
	
	menu_rect = menu_.get_rect(topleft=(18,30))
	exit_dosk_rect = dosk_exit.get_rect(topleft=(-600 + exit_dosk, 0))
	
	setup_rect = setup_button.get_rect(topleft=(35 - x_dosk, 500))
	
	home_rect = home_button.get_rect(topleft=(35 - x_dosk, 290))
	
	info_dosk_rect = info_dosk_button.get_rect(topleft=(35 - x_dosk,1600))
	
	exit_rect = exit_button.get_rect(topleft=(35- x_dosk,1800))
	
	setting_rect = setting_button.get_rect(topleft=(35- x_dosk,1400))
	
	secret_rect = secret_button.get_rect(topleft=(35- x_dosk,1200))
	
	if menu_rect.collidepoint(mouse) and x_dosk >= 50:
		dosk_act = True
			
	if exit_dosk_rect.collidepoint(mouse) and run == False and not act_dosk == True:
		act_dosk = True
			
	if setup_rect.collidepoint(mouse) and run == False:
		home = "setup"
		act_dosk = True
		
	if home_rect.collidepoint(mouse) and run == False:
		home = "home"
		run = True
		act_dosk = True
	
	if setting_rect.collidepoint(mouse) and run == False:
		home = "setting"
		run = True
		act_dosk = True
	
	if secret_rect.collidepoint(mouse) and run == False:
		home = "secret_password"
		run = True
		act_dosk = True
		
	if info_dosk_rect.collidepoint(mouse) and run == False:
		if one_point == 1:
			if not home == "exit":
				home_copy = home
			one_point = 0
		home = "info"
		act_dosk = True
	
	if exit_rect.collidepoint(mouse) and run == False:
		if one_point_ == 1:
			if not home == "info":
				home_copy = home
			one_point_ = 0
		home = "exit"
		act_dosk = True
	
	if info_rect.collidepoint(mouse) and run == True:
		if one_point == 1:
			home_copy = home
			one_point = 0
		info_exit = 1000
		home = "info"
		act_dosk = True
	
	if act_dosk == True:
		for i in range(60):
			x_dosk += 0.7
			if x_dosk >= 550:
				run = True
				exit_dosk = -50
				x_dosk = 550
				act_dosk = False
				
	if dosk_act == True:
		exit_dosk = 1190
		color = 100
		for i in range(60): 
			x_dosk -= 0.8
			panel = None
			if x_dosk <= 0:
				run = False
				x_dosk = -10
				dosk_act = False
	
	if home_copy == "exit":
		home == "home"
				
	if home == "home":
		screen.blit(home1_1_txt,(640-x_dosk, 900))
		screen.blit(home1_2_txt,(675-x_dosk, 1015))
		screen.blit(home2_1_txt,(600-x_dosk, 1780))
		screen.blit(home2_2_txt,(600-x_dosk, 1860))
		screen.blit(home2_3_txt,(800-x_dosk, 1950))
		
	if home == "info":
		info_rect_ = info_button_.get_rect(topleft=(1280 - x_dosk,55))
		mail_rect = mail_button.get_rect(topleft=(785-x_dosk,475))
		copy_rect = copy_png_.get_rect(topleft=(1525-x_dosk,490))
		
		screen.blit(info_dosk2, (565-x_dosk,230))
		screen.blit(info_dosk, (580-x_dosk,245))
		screen.blit(info_exit_txt, (1300-x_dosk,75))
		screen.blit(info1_txt, (615-x_dosk,385))
		screen.blit(info2_txt, (860-x_dosk,290))
		
		screen.blit(info3_1_txt, (615-x_dosk,610))
		screen.blit(info3_2_txt, (615-x_dosk,710))
		screen.blit(info3_3_txt, (615-x_dosk,810))
		screen.blit(info3_4_txt, (615-x_dosk,910))
		screen.blit(info3_5_txt, (615-x_dosk,1010))
		screen.blit(info4_1_txt, (615-x_dosk,500))
		screen.blit(info4_2_txt, (800-x_dosk,500))
		screen.blit(copy_png, (1535-x_dosk,500))
		screen.blit(info5_txt, (615-x_dosk,1205))
		screen.blit(info6_txt, (615-x_dosk,1305))
		
		if info_rect_.collidepoint(mouse) and run == True:
			home = home_copy
		if mail_rect.collidepoint(mouse):
			w.open("https://mail.google.com/mail/mu/mp/660/#co")
		if copy_rect.collidepoint(mouse):
			w.open("https://disk.yandex.ru/d/x1kKBBWf2ZhhmA")
	else:
		one_point = 1
			
	if home == "setup":
		setup_calc_rect = setup_calc.get_rect(topleft=(640 - x_dosk,280))
		setup_setupyt_rect = setup_setupyt.get_rect(topleft=(1180 - x_dosk,280))
		
		if pygame.mouse.get_pressed()[0]:
		    mouse = pygame.mouse.get_pos()
		else:
		    mouse = (9999999,999999)
		
		screen.blit(setup_calc,(670-x_dosk,280))
		screen.blit(setup_calc_,(680-x_dosk,290))
		
		screen.blit(setup_setupyt,(1180-x_dosk,280))
		screen.blit(setup_setupyt_,(1190-x_dosk,290))
		
		screen.blit(calc_png,(710-x_dosk,320))
		screen.blit(setupyt_png,(1217-x_dosk,320))
		
		screen.blit(calc_txt,(730-x_dosk,620))
		screen.blit(setupyt_txt,(1230-x_dosk,620))
		
		screen.blit(setupy_txt,(635-x_dosk,1857))
		screen.blit(setupy1_txt,(645-x_dosk,1940))
		
		mouse_act = True
		
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONUP:
				if setup_calc_rect.collidepoint(mouse) and run == True:
					mouse_stop = True
					w.open("https://disk.yandex.com/d/L7MMYAo5KRYOQA(")
			
	if home == "exit":
		no_button_rect = no_button.get_rect(topleft=(800-x_dosk,960))
		yes_button_rect = yes_button.get_rect(topleft=(1150-x_dosk,960))
		
		screen.blit(exit_panel_,(640 - x_dosk,700))
		screen.blit(exit_panel,(650 - x_dosk,710))
		screen.blit(exit_exit_txt,(850 - x_dosk,730))
		screen.blit(exit_exit1_txt,(750 - x_dosk,815))
		screen.blit(no_button_,(790 - x_dosk,950))
		screen.blit(no_button,(800 - x_dosk,960))
		screen.blit(yes_button_,(1140 - x_dosk,950))
		screen.blit(yes_button,(1150 - x_dosk,960))
		screen.blit(yes_txt,(1200 - x_dosk,980))
		screen.blit(no_txt,(840 - x_dosk,980))
		for event in pygame.event.get():
     		 if event.type == pygame.MOUSEBUTTONUP:
     		 	if no_button_rect.collidepoint(mouse) and run == True:
     		 		home = home_copy
		
		if yes_button_rect.collidepoint(mouse) and run == True:
			running = False
	else:
		one_point_ = 1
			
	if home == "setting":
		setting_color_rect = setting_color.get_rect(topleft=(925 -x_dosk, 950))
		
		screen.blit(setting_color,(925-x_dosk, 950))
		
		if setting_color_rect.collidepoint(mouse) and run == True:
			panel = "color"
			txt_color_30 = (220,220,220)
			txt_color_60 = (190,190,190)
			txt_color_90 = (160,160,160)
			txt_color_140 = ()
			
			button_color_90 = (50,50,50)
			button_color_140 = (110,110,110)
			
			app_color = (50,100,150)
			screen_color = (105,105,105)
			info_dosk_color = (80,80,80)
			info_dosk2_color = (60,60,60)
			exit_panel_color = (120,120,120)
			exit_panel_color_ = (60,60,60)
		
	if home == "secret_password":

		one_password_rect = one_num.get_rect(topleft=(770 -x_dosk, 1100))
		two_password_rect = two_num.get_rect(topleft=(995 -x_dosk, 1100))
		tree_password_rect = tree_num.get_rect(topleft=(1220 -x_dosk, 1100))
		
		four_password_rect = four_num.get_rect(topleft=(770 -x_dosk, 1320))
		five_password_rect = five_num.get_rect(topleft=(995 -x_dosk, 1320))
		six_password_rect = six_num.get_rect(topleft=(1220 -x_dosk,1320 ))
		
		seven_password_rect = seven_num.get_rect(topleft=(770 -x_dosk, 1540))
		eight_password_rect = eight_num.get_rect(topleft=( 995-x_dosk, 1540))
		nine_password_rect = nine_num.get_rect(topleft=(1220 -x_dosk, 1540))
		
		zero_password_rect = zero_num.get_rect(topleft=(995 -x_dosk, 1760))
		delet_password_rect = delet_num.get_rect(topleft=(770 -x_dosk, 1760))
		enter_password_rect = delet_num.get_rect(topleft=(1220 -x_dosk, 1760))

		screen.blit(one_num,(770 - x_dosk,1100))
		screen.blit(two_num,(995 - x_dosk,1100))
		screen.blit(tree_num,(1220- x_dosk,1100))
		
		screen.blit(four_num,(770 - x_dosk,1320))
		screen.blit(five_num,(995 - x_dosk,1320))
		screen.blit(six_num,(1220- x_dosk,1320))
		
		screen.blit(seven_num,(770 - x_dosk,1540))
		screen.blit(eight_num,(995 - x_dosk,1540))
		screen.blit(nine_num,(1220- x_dosk,1540))
		
		screen.blit(zero_num,(995- x_dosk,1760))
		screen.blit(delet_num,(770- x_dosk,1760))
		screen.blit(enter_num,(1220- x_dosk,1760))
		
		screen.blit(num_button,(780- x_dosk,1110))
		screen.blit(num_button,(1005- x_dosk,1110))
		screen.blit(num_button,(1230- x_dosk,1110))
		screen.blit(num_button,(780- x_dosk,1330))
		screen.blit(num_button,(1005- x_dosk,1330))
		screen.blit(num_button,(1230- x_dosk,1330))
		screen.blit(num_button,(780- x_dosk,1550))
		screen.blit(num_button,(1005- x_dosk,1550))
		screen.blit(num_button,(1230- x_dosk,1550))
		screen.blit(num_button,(1005- x_dosk,1770))
		screen.blit(num_button,(1230- x_dosk,1770))
		screen.blit(num_button,(780- x_dosk,1770))
		
		screen.blit(one_txt,(820- x_dosk,1135))
		screen.blit(two_txt,(1050- x_dosk,1135))
		screen.blit(tree_txt,(1270- x_dosk,1135))
		
		screen.blit(four_txt,(820- x_dosk,1355))
		screen.blit(five_txt,(1050- x_dosk,1355))
		screen.blit(six_txt,(1270- x_dosk,1355))
		screen.blit(info_exit_txt,(795 - x_dosk,1805))
		screen.blit(enter_txt,(1245 - x_dosk,1805))
		
		screen.blit(seven_txt,(820- x_dosk,1575))
		screen.blit(eight_txt,(1050- x_dosk,1575))
		screen.blit(nine_txt,(1270- x_dosk,1575))
		screen.blit(zero_txt,(1050- x_dosk,1795))
		
		screen.blit(panel_num,(770- x_dosk,680))
		screen.blit(panel_num_,(780- x_dosk,690))
		
		for event in pygame.event.get():
			    if enter_password_rect.collidepoint(mouse) and run == True:
			    	if password == "2005320" or password == "1010031":
			    		home = "secret"
			    	else:
			    		password = ""
			    		
			    if event.type == pygame.MOUSEBUTTONUP:
		    		if len(password) < 8:
			    		if one_password_rect.collidepoint(mouse) and run == True:
			    			user = "1"
			    			mouse_act = False
			    		if two_password_rect.collidepoint(mouse) and run == True:
			    			user = "2"
			    		if tree_password_rect.collidepoint(mouse) and run == True:
			    			user = "3"
			    		if four_password_rect.collidepoint(mouse) and run == True:
			    			user = "4"
			    		if five_password_rect.collidepoint(mouse) and run == True:
			    			user = "5"
			    		if six_password_rect.collidepoint(mouse) and run == True:
			    			user = "6"
			    		if seven_password_rect.collidepoint(mouse) and run == True:
			    			user = "7"
			    		if eight_password_rect.collidepoint(mouse) and run == True:
			    			user = "8"
			    		if nine_password_rect.collidepoint(mouse) and run == True:
			    			user = "9"
			    		if zero_password_rect.collidepoint(mouse) and run == True:
			    			user = "0"
			    	if delet_password_rect.collidepoint(mouse) and run == True:
				   		password = password[:-1]
		    			
		password = str(password+user)
		
		if len(password) < 8:
			password_ = str(password+"_")
		else:
			password_ = password
			
		user = ""
		
		password_txt = txt___.render(password_, False,  (210,210,210))
		
		screen.blit(password_txt,(795- x_dosk,705))
	elif home == "secret":
		password = ""
		
	if home == "secret":
		secret_divan_rect = secret_divan.get_rect(topleft=(605 - x_dosk,280))
		
		screen.blit(secret_divan,(605-x_dosk, 280))
		screen.blit(secret_divan_,(615-x_dosk, 290))
		if secret_divan_rect.collidepoint(mouse) and run == True:
			w.open("https://hot.noodlemagazine.com/watch/-181134945_456239017")
		
	for event in pygame.event.get():
      	 if event.type == pygame.QUIT:
      	 	running = False
      	 	pygame.quit()

	pygame.display.update()
