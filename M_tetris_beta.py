import pygame , random , sys , pickle
pygame.init()
win=pygame.display.set_mode((1200 , 700 ),pygame.FULLSCREEN)
pygame.display.set_caption('Mtetris_beta')
def shape_saz(full):
    for m_y in range(27):
        for m_x in range(24):
            pygame.draw.rect(win,(50,50,50), (26 * m_x, 26 * m_y, 25, 25))
    for U in full:
        color = [U[0] // 3, (1 + U[1]) // 3, (1 + U[1]) // 3]
        pygame.draw.rect(win ,color ,(U[0],U[1],25,25) )
def dinamik_shape(full,color):
    for U in full:
        pygame.draw.rect(win ,color ,(U[0],U[1],25,25) )
def all_max(x,y,list_1,rot):
    list_p = list_1
    if rot == 0:
        list_x = list_1
    elif rot == 1:
        list_x=[]
        for mx in list_p:
            if mx == 1:
                list_x.append(7)
            elif mx == 9:
                list_x.append(3)
            elif mx == 8:
                list_x.append(6)
            elif mx == 7:
                list_x.append(9)
            elif mx == 6:
                list_x.append(2)
            elif mx == 5:
                list_x.append(5)
            elif mx == 4:
                list_x.append(8)
            elif mx == 3:
                list_x.append(1)
            elif mx == 2:
                list_x.append(4)
    elif rot == 2:
        list_x=[]
        for mx in list_1:
            if mx == 1:
                list_x.append(9)
            elif mx == 2:
                list_x.append(8)
            elif mx == 3:
                list_x.append(7)
            elif mx == 4:
                list_x.append(6)
            elif mx == 5:
                list_x.append(5)
            elif mx == 6:
                list_x.append(4)
            elif mx == 7:
                list_x.append(3)
            elif mx == 8:
                list_x.append(2)
            elif mx == 9:
                list_x.append(1)
    elif rot == 3:
        list_x=[]
        for mx in list_1:
            if mx == 1:
                list_x.append(3)
            elif mx == 2:
                list_x.append(6)
            elif mx == 3:
                list_x.append(9)
            elif mx == 4:
                list_x.append(2)
            elif mx == 5:
                list_x.append(5)
            elif mx == 6:
                list_x.append(8)
            elif mx == 7:
                list_x.append(1)
            elif mx == 8:
                list_x.append(4)
            elif mx == 9:
                list_x.append(7)
    awr = []
    for lx in list_x:
        if lx == 1:
            awr.append([x-26,y-26])
        elif lx == 2:
            awr.append([x,y-26])
        elif lx == 3 :
            awr.append([x+26,y-26])
        elif lx == 4 :
            awr.append([x-26,y])
        elif lx == 5 :
            awr.append([x,y])
        elif lx == 6 :
            awr.append([x+26,y])
        elif lx == 7 :
            awr.append([x-26,y+26])
        elif lx == 8 :
            awr.append([x,y+26])
        elif lx == 9 :
            awr.append([x+26,y+26])
    return awr
def all_full(x,y,ship_type,r):
    if ship_type == 1 :
        if r== 0 :
            awr =[[x,y],[x+26,y]]
        elif r == 1 :
            awr = [[x,y],[x,y-26]]
    elif ship_type == 2 :
        awr = [[x,y],[x+26,y],[x,y+26],[x+26,y+26]]
    elif ship_type == 3 :
        if r== 0:
            awr = [[x,y],[x+26,y],[x+26,y+26],[x+52,y+26]]
        elif r== 1 :
            awr = [[x,y],[x,y+26],[x-26,y+26],[x-26,y+52]]
    elif ship_type == 4 :
        if r == 0 :
            awr = [[x,y],[x-26,y],[x-26,y+26],[x-52,y+26]]
        elif r == 1 :
            awr = [[x,y],[x, y +26 ],[x+26,y+26],[x+26,y+52]]
    elif ship_type == 5 :
        if r == 0 :
            awr =[[x,y],[x+26,y],[x+52,y],[x+78,y]]
        elif r== 1 :
            awr =[[x,y],[x,y+26],[x,y+52],[x,y+78]]
    elif ship_type == 6 :
        if r == 0 :
            awr = [[x,y],[x,y+26],[x+26,y+26]]
        elif r==1 :
            awr = [[x,y],[x-26,y],[x-26,y+26]]
        elif r == 2:
            awr = [[x,y],[x-26,y],[x, y+26]]
        elif r== 3:
            awr = [[x, y],[x  , y +26],[x -26, y+26]]
    elif ship_type == 7 :
        if r == 0 :
            awr =[[x, y],[x  , y +26],[x +26, y+26],[x +52, y+26]]
        elif r== 1 :
            awr =[[x,y],[x+26, y],[x, y+26],[x, y+52]]
        elif r== 2 :
            awr =[[x, y+26],[x,y],[x-26, y],[x-52, y]]
        elif r== 3 :
            awr =[[x-26, y+26],[x, y-26],[x, y],[x, y+26]]
    elif ship_type == 8 :
        if r == 0 :
            awr =[[x+52,y],[x,y+26],[x +26, y+26],[x +52, y+26]]
        elif r== 1 :
            awr =[[x,y],[x+26,y+52],[x, y+26],[x, y+52]]
        elif r== 2 :
            awr =[[x-26,y+26],[x,y],[x+26, y],[x-26, y]]
        elif r== 3 :
            awr =[[x-26, y-26],[x, y-26],[x, y],[x, y+26]]
    return awr
def bottom_chek(astatik,dinamik):
    bottom_move = True
    for din in dinamik :
        if [din[0],din[1]+26] in astatik :
            bottom_move = False
        if bottom_move == True and din[1] == 676 :
            bottom_move = False
    return bottom_move
def right_chek(astatik,dinamik):
    right_move = True
    for din in dinamik :
        if [din[0] +26 ,din[1]] in astatik:
            right_move = False
        if right_move == True and din[0] == 598 :
            right_move=False
    return right_move
def left_chek(astatik,dinamik):
    left_move = True
    for din in dinamik :
        if [din[0] -26 ,din[1]] in astatik :
            left_move = False
        if left_move == True and din[0] == 0 :
            left_move = False
    return left_move
def rotation_chek(astatik,dinamik):
    rotation = True
    for din in  dinamik :
        if din in astatik :
            rotation = False
        if rotation == True and (din[0]> 598 or din[0]< 0 or din[1]>676):
            rotation = False
    return rotation
def del_line(lines,d_n):
    awr=[]
    for box in lines:
        if box[1] in d_n :
          o=0
        else:
            awr.append(box)
    for sortin in d_n :
        for fa_wr in awr :
            if fa_wr[1] < sortin:
                fa_wr[1] += 26
    return awr
def full_line(boxs_list):
    line_for_del = []
    lines=[0]*27
    for f_m in boxs_list :
        lines[(f_m[1]+26)//26 - 2] += 1
    for i in range(0,26):
        if lines[i]== 24:
            line_for_del.append((i*26)+26)
    if len(line_for_del)>0 :
        return [True ,sorted(line_for_del)]
    else:
        return [False]
    debug=False
    for s_box1 in s_box :
        cont=-1
        for s_box2 in s_box :
            cont+=1
            if s_box2[0]+26 !=s_box[0] and s_box2[0]-26 != s_box1[0] and s_box2[1]+26 != s_box1[1]:
                s_box[cont][1] +=26
    return s_box
def game_over(full,y):
    game_over=False
    if y == 0 :
        for fu in full :
            if (y+26) == fu[1]:
                game_over = True
    return game_over
def next_shape_fn(ns):
    for next in ns:
        pygame.draw.rect(win , (0,0,0), (next[0],next[1],25,25))
def message_to_display(msg, x_y,color):
    pygame.draw.rect(win , (25,48,52),(x_y[0]-10,x_y[1]-5,500,35))
    pygame.draw.rect(win , color,(x_y[0]-10,x_y[1]-5,500,35),2)
    font = pygame.font.SysFont(None, 35)
    screen_text = font.render(msg, True, [0,0,0])
    win.blit(screen_text, [x_y[0]-3,x_y[1]+3])
    screen_text = font.render(msg, True, [255,255,255])
    win.blit(screen_text, x_y)
def logo(msg, x_y,color):
    font = pygame.font.SysFont(None, 200)
    screen_text = font.render(msg, True, color)
    screen_text2 = font.render(msg, True, (0,0,0))
    win.blit(screen_text2, [x_y[0]-3,x_y[1]+3])
    win.blit(screen_text, x_y)
def Game_Over_display(score):
    wb = 1
    font = pygame.font.SysFont(None, 150)
    font2 = pygame.font.SysFont(None, 80)
    screen_text = font.render('Game Over', True, [0,0,0])

    for i in range(700):

        if wb ==1:
            wb = 2
            screen_text = font.render('Game Over', True, [0, 0, 255])
            win.blit(screen_text, [301, 199])

        elif wb == 2:
            screen_text = font.render('Game Over', True, [0, 255, 0])
            win.blit(screen_text, [299, 202])
            wb= 3
        elif wb == 3:
            wb = 4
            screen_text = font.render('Game Over', True, [255, 0, 0])
            win.blit(screen_text, [303, 198])
        else:
            wb = 1
            win.fill((10,100,80))
            screen_text = font.render('Game Over', True, [255, 255, 255])
            win.blit(screen_text, [300, 200])
        pygame.display.update()
    screen_text2 = font2.render('score : ' + str(score), True, [0, 0, 0])
    screen_text = font2.render('score : ' + str(score), True, [255, 255, 255])
    pygame.time.delay(500)
    win.blit(screen_text2, [418, 403])
    win.blit(screen_text, [420, 400])

    pygame.display.update()
    pygame.time.delay(1200)
    win.fill((255, 255, 255))
def btn(select):
    color1=(255,0,0)
    color2=(255,120,0)
    if select == 0 :
        pygame.draw.rect(win,color2,(350,300,490,70))
        pygame.draw.rect(win,color1,(350,400,490,70))
        pygame.draw.rect(win,color1,(350,500,490,70))
    if select == 1 :
        pygame.draw.rect(win,color1,(350,300,490,70))
        pygame.draw.rect(win,color2,(350,400,490,70))
        pygame.draw.rect(win,color1,(350,500,490,70))
    if select == 2 :
        pygame.draw.rect(win,color1,(350,300,490,70))
        pygame.draw.rect(win,color1,(350,400,490,70))
        pygame.draw.rect(win,color2,(350,500,490,70))
    font = pygame.font.SysFont(None, 60)
    screen_text = font.render('Classic', True, [255, 255 , 255])
    screen_text2 = font.render('Create New Game', True, [255, 255 , 255])
    screen_text3 = font.render('Exit', True, [255, 255 , 255])
    win.blit(screen_text, [515, 315])
    win.blit(screen_text2, [410, 415])
    win.blit(screen_text3, [555, 515])
    font2 = pygame.font.SysFont(None, 40)
    screen_text4 = font2.render('insta:mohammad.ra9 _ mohammad.ra.31.11@gmail.com', True, [20, 20 , 20])
    win.blit(screen_text4, [10, 670])
def mine(mod1,shape_list):
    mod = mod1
    ha1 = 200
    ha2 = 1
    ha3 = 100
    win.fill((10,10,10))
    x = 286
    y = 0
    s_r = 0
    score = 0
    if mod == 0 :
        rand_num = random.randint(1, 8)
        next_3 = random.randint(1, 8)
        next_2 = random.randint(1, 8)
        next_shape = random.randint(1, 8)

    else:
        rand_lim = shape_list[-1] - 1
        rand_num = random.randint(0, rand_lim)
        next_3 = random.randint(0,rand_lim)
        next_2 = random.randint(0, rand_lim)
        next_shape = random.randint(0, rand_lim)

    run1 = True

    full_box = []
    time_conter = 0
    if mod == 0 or (mod == 1 and shape_list[-2]=="r"):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    while run1 :
        if time_conter == 80:
            y+=26
            time_conter=0
        if mod == 0:
            shape_matrix = all_full(x, y, rand_num, s_r)
        else:
            shape_matrix = all_max(x, y, shape_list[0][rand_num], s_r)
            if shape_list[-2] == "c":
                color = shape_list[0][rand_num + shape_list[-1]]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run1 = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run1 = False
                if event.key == pygame.K_z  :

                    if mod == 0 and left_chek(full_box, shape_matrix) == True and left_chek(full_box, all_full(x -26 , y, rand_num, s_r)) == True:
                        x -= 52
                if event.key == pygame.K_x  :
                    if mod== 0 and right_chek(full_box, shape_matrix) == True and right_chek(full_box, all_full(x+26, y, rand_num, s_r)) == True:
                        x += 52
                if event.key == pygame.K_LEFT:
                    if left_chek(full_box, shape_matrix) == True:
                        x -= 26
                if event.key == pygame.K_RIGHT:
                    if right_chek(full_box, shape_matrix) == True:
                        x += 26
                if event.key == pygame.K_DOWN:
                    if bottom_chek(full_box, shape_matrix) == True:
                        y += 26
                if mod == 1 :
                    if event.key ==pygame.K_UP:
                        if s_r==0 and rotation_chek(full_box,all_max(x,y,shape_matrix, 3 )) == True:
                            s_r=3
                        elif(s_r==1) and rotation_chek(full_box,all_max(x,y,shape_matrix, 0 )) == True:
                            s_r=0
                        elif(s_r==2)  and rotation_chek(full_box,all_max(x,y,shape_matrix, 1 )) == True  :
                                s_r=1
                        elif s_r==3 and rotation_chek(full_box,all_max(x,y,shape_matrix, 2 )) == True:
                            s_r=2
                # 1--------------------------------------------------------

                if mod == 0 and rand_num == 1:
                    if event.key ==pygame.K_UP:
                        if s_r==0 and rotation_chek(full_box,all_full(x,y,rand_num, 1 )) == True  :
                            s_r=1
                        elif s_r==1 and rotation_chek(full_box,all_full(x,y,rand_num, 0 )) == True :
                            if x<575:
                                s_r=0
    # 2--------------------------------------------------------

                elif mod == 0 and rand_num == 3 :
                    if event.key == pygame.K_UP :
                        if s_r == 0 and rotation_chek(full_box,all_full(x,y,rand_num, 1 )) == True:
                            s_r=1
                            n_y = 2
                        elif(s_r==1 and rotation_chek(full_box,all_full(x,y,rand_num, 0 )) == True ):
                            s_r=0
                            n_y = 1
     # 4--------------------------------------------------------

                elif  mod == 0 and rand_num == 4 :
                    if event.key == pygame.K_UP :
                        if s_r == 0 and rotation_chek(full_box,all_full(x,y,rand_num, 1 )) == True :
                            s_r=1
                        elif(s_r==1and rotation_chek(full_box,all_full(x,y,rand_num, 0 )) == True ):
                            s_r=0
    # 5--------------------------------------------------------

                elif  mod == 0 and  rand_num == 5 :
                    if event.key == pygame.K_UP :
                        if s_r == 0 and rotation_chek(full_box,all_full(x,y,rand_num, 1 )) == True:
                            s_r=1
                        elif(s_r==1 and rotation_chek(full_box,all_full(x,y,rand_num, 0 )) == True ):
                            s_r=0
    # 6--------------------------------------------------------

                if  mod == 0 and  rand_num == 6:
                    if event.key ==pygame.K_UP:
                        if s_r==0 and rotation_chek(full_box,all_full(x,y,rand_num, 1 )) == True:
                            s_r=1
                        elif(s_r==1 and rotation_chek(full_box,all_full(x,y,rand_num, 2 )) == True):
                            s_r=2
                        elif(s_r==2 and rotation_chek(full_box,all_full(x,y,rand_num, 3 )) == True):
                                s_r=3
                        elif (s_r == 3) and rotation_chek(full_box,all_full(x,y,rand_num, 0 )) == True:
                            s_r=0


     # 7--------------------------------------------------------
                if  mod == 0 and  rand_num == 7:
                    if event.key ==pygame.K_UP:
                        if s_r==0 and rotation_chek(full_box,all_full(x,y,rand_num, 1 )) == True:
                            s_r=1
                        elif(s_r==1) and rotation_chek(full_box,all_full(x,y,rand_num, 2 )) == True:
                            s_r=2
                        elif(s_r==2)  and rotation_chek(full_box,all_full(x,y,rand_num, 3 )) == True  :
                                s_r=3
                        elif s_r==3 and rotation_chek(full_box,all_full(x,y,rand_num, 0 )) == True:
                            s_r=0
        # 8--------------------------------------------------------

                if  mod == 0 and  rand_num == 8:
                    if event.key ==pygame.K_UP:
                        if s_r==0 and rotation_chek(full_box,all_full(x,y,rand_num, 1 )) == True:
                            s_r=1
                        elif(s_r==1) and rotation_chek(full_box,all_full(x,y,rand_num, 2 )) == True :
                            s_r=2
                        elif(s_r==2) and rotation_chek(full_box,all_full(x,y,rand_num, 3 )) == True :
                                s_r=3
                        elif s_r==3 and rotation_chek(full_box,all_full(x,y,rand_num, 0 )) == True :
                            s_r=0

        if  bottom_chek(full_box,shape_matrix) == False:
            full_box += shape_matrix
            score += 50
            rand_num = next_shape
            next_shape = next_2
            next_2 = next_3
            if mod == 0:
                next_3 =random.randint(1, 8)
            else:
                next_3 = random.randint(1,rand_lim)
                if game_over(full_box, y) == True:
                    run1 = False
            clean = full_line(full_box)[0]
            if mod == 0 or (mod==1 and shape_list[-2]=='r'):
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            if clean == True :
                full_box = del_line(full_box,full_line(full_box)[1])
                score += 150
                clean =False

            x = 286
            y = 0
            s_r = 0
        if game_over(full_box, y) == False:

            shape_saz(full_box)
            dinamik_shape(shape_matrix,color)

        pygame.time.delay(1)
        time_conter += 1
        if next_shape == 1 or next_shape == 5 :
            xp = 65
        else:
            xp = 50
        if next_2 == 1 or next_2 == 5 :
            xp2 = 65
        else:
            xp2 = 50
        if next_3 == 1 or next_3 == 5 :
            xp3 = 65
        else:
            xp3 = 50
        pygame.draw.rect(win, (255, 255 , 255), (650, 20, 550, 120))
        pygame.draw.rect(win, color , (650, 20, 600, 120),5)
        pygame.draw.rect(win, (100,100,100) , (652, 22, 600, 116),2)
        if mod == 0:
            next_shape_fn(all_full(1080,xp3,next_3,0))
            next_shape_fn(all_full(900,xp2,next_2,0))
            next_shape_fn(all_full(720,xp,next_shape,0))
        else:
            next_shape_fn(all_max(1080,65,shape_list[0][next_3],0))
            next_shape_fn(all_max(900,65,shape_list[0][next_2],0))
            next_shape_fn(all_max(720,65,shape_list[0][next_shape],0))
        message_to_display('Your Score ' , [660,160],color)
        message_to_display(str(score) , [810,160],color)

        pygame.display.update()
    win.fill((255, 255, 255))
    return score
def Meno():
    select = 0
    coco1 = 0
    score = 0
    showbtn=False
    win.fill((255, 255, 255))
    meno = True
    coco=[(255,255,255)]*6
    while meno:

        logo('T', [400, 150],coco[0])
        logo('E', [460, 150],coco[1])
        logo('T', [530, 150],coco[2])
        logo('R', [600, 150],coco[3])
        logo('I', [680, 150],coco[4])
        logo('S', [700, 150],coco[5])
        pygame.time.delay(1)
        coco1 += 1
        if coco1 == 30:
            coco[5]=coco[4]
        elif coco1 == 40 :
            coco[4]=coco[3]
        elif coco1 == 50 :
            coco[3]=coco[2]
        elif coco1 == 60:
            coco[2] = coco[1]
        elif coco1 == 70:
            coco[1] = coco[0]
        elif coco1 == 80:
            coco1 = 0
            coco[0]=(random.randint(0,250),random.randint(0,250),random.randint(0,250))
        btn(select)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                meno = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    if select <2 :
                        select += 1
                if event.key == pygame.K_UP:
                    if select >0:
                        select -= 1
                if event.key == pygame.K_SPACE:
                    if select == 0:
                        score = mine(0,[])
                        Game_Over_display(score)
                    elif select == 1 :
                        x=game_creater()
                        if x[0]==True:
                            score = mine(1,x[1])
                            Game_Over_display(score)
                    elif select == 2:
                        meno = False

        pygame.display.update()
def obj_loct(selected,target,event,sh_list_d,tod):
    color1 = [(80, 80, 80)] * 12
    color2 = [(80, 80, 80)] * 12

    if tod == 1:
        if selected >= 0 and selected<= 11 :
            if target == False :
                color1[selected] = (255, 255, 255)
            else:
                color1[selected] = (150, 255, 200)
                if sh_list_d.count(event) < 1 and event != 0 :
                    sh_list_d += [event]
                elif sh_list_d.count(event) == 1:
                    sh_list_d.remove(event)

    elif tod == 2:
        if target == False:
            color2[selected] = (255, 255, 255)
        else:
            color2[selected] = (150, 255, 200)
            if sh_list_d.count(event) < 1 and event != 0:
                sh_list_d += [event]
            elif sh_list_d.count(event) == 1:
                sh_list_d.remove(event)

    for sh_nu in range(12):
        big_mar = sh_nu * 94 + 18
        pygame.draw.rect(win, color1[sh_nu], (big_mar + 20, 20, 92, 92))
        for co1 in range(0, 3):
            for co2 in range(0, 3):
                x_mar = co1 * 30 + big_mar
                y_mar = co2 * 30
                pygame.draw.rect(win, (200, 200, 200), (x_mar + 22, y_mar + 22, 28, 28))

    for sh_nu in range(12):
        big_mar = sh_nu * 94 + 18
        pygame.draw.rect(win, color2[sh_nu], (big_mar + 20, 120, 92, 92))
        for co1 in range(0, 3):
            for co2 in range(0, 3):
                x_mar = co1 * 30 + big_mar
                y_mar = co2 * 30
                pygame.draw.rect(win, (200, 200, 200), (x_mar + 22, y_mar + 122, 28, 28))

    return sh_list_d
def ch_box_top(li):
    for cbt in range(12):
        for lcbt in li[cbt]:
            if lcbt == 1 or lcbt == 2 or lcbt == 3:
                top_mar = 22
            elif lcbt == 4 or lcbt == 5 or lcbt == 6:
                top_mar = 52
            else:
                top_mar = 82
            if lcbt == 1 or lcbt == 4 or lcbt == 7:
                left_z = 30
            elif lcbt == 2 or lcbt == 5 or lcbt == 8:
                left_z = 60
            else:
                left_z = 90
            pygame.draw.rect(win,(255,0,0),((94*cbt+10)+left_z,top_mar,28,28))
def ch_box_top2(li):
    for cbt in range(12):
        for lcbt in li[cbt]:
            if lcbt == 1 or lcbt == 2 or lcbt == 3:
                top_mar = 22
            elif lcbt == 4 or lcbt == 5 or lcbt == 6:
                top_mar = 52
            else:
                top_mar = 82
            if lcbt == 1 or lcbt == 4 or lcbt == 7:
                left_z = 30
            elif lcbt == 2 or lcbt == 5 or lcbt == 8:
                left_z = 60
            else:
                left_z = 90
            pygame.draw.rect(win,(255,0,0),((94*cbt+10)+left_z,top_mar+100,28,28))
def next_ok_btn(hover):
    font = pygame.font.SysFont(None, 50)
    if hover == False :
        pygame.draw.rect(win, (35,35,55), (40,220,130,85))
        pygame.draw.rect(win, (35,40,60), (45,225,120,75))
        pygame.draw.rect(win, (35,45,65), (50,230,110,65))
        pygame.draw.rect(win, (35,50,70), (55,235,100,55))
        pygame.draw.rect(win, (35,55,75), (60,240,90,45))
        screen_text = font.render('Next',True,(55,80,100))
    else:
        pygame.draw.rect(win, (35,55,75), (40,220,130,85))
        pygame.draw.rect(win, (35,50,70), (45,225,120,75))
        pygame.draw.rect(win, (35,45,65), (50,230,110,65))
        pygame.draw.rect(win, (35,40,60), (55,235,100,55))
        pygame.draw.rect(win, (35,35,55), (60,240,90,45))
        screen_text = font.render('Next',True,(15,10,35))

    win.blit(screen_text,[67,245])
def full_shape(list1,list2):
    list3 = list1 + list2

    for i in range(list3.count([])) :
        list3.remove([])

    return list3
def color_tool_bar(hover,step,c_c_d,rand_color,color_cunt):
    btnscolor=[(25,25,25),(0,0,0),(150,150,150),(180,180,180),(180,180,180),(180,180,180)]
    if hover :
        btnscolor[0]=(200,200,200)
    if step== 1:
        btnscolor[1]=(255,255,255)
    else:
        btnscolor[1]=(0,0,0)
    pygame.draw.rect(win,btnscolor[0],(180,220,985,85))
    font = pygame.font.SysFont(None, 30)
    screen_text = font.render('Random color', True, (100, 130, 160))
    pygame.draw.rect(win,btnscolor[1],(200,240,200,40))
    win.blit(screen_text,[210,250])
    pygame.draw.rect(win,(100, 130,  160),(365,245,30,30))
    pygame.draw.rect(win, btnscolor[1], (370, 250, 20, 20),5)
    pygame.draw.rect(win,btnscolor[2],(450,227,500,70))

    if rand_color == False:
        font2 = pygame.font.SysFont(None, 33)
        screen_text2= font2.render('Shape number ' + str(color_cunt + 1), True, (50, 50, 50))
        pygame.draw.rect(win,(255,255,255),(370, 250, 20, 20))
        btnscolor[3]=(255,150,150)
        btnscolor[4] = (150, 255, 150)
        btnscolor[5] = (150, 150, 255)
        win.blit(screen_text2, [700, 251])
        if step == 2:
            btnscolor[3] = (255, 0, 0)
        elif step == 3:
            btnscolor[4] = (0, 255, 0)
        elif step == 4:
            btnscolor[5] = (0,0,255)

    else:
        btnscolor[3]=(180,180,180)
        btnscolor[4] = (180, 180, 180)
        btnscolor[5] = (180, 180, 180)
    pygame.draw.rect(win,(btnscolor[3]),(460,246,70,32))
    pygame.draw.rect(win,(btnscolor[4]),(540,246,70,32))
    pygame.draw.rect(win,(btnscolor[5]),(620,246,70,32))
    if step == 5 :
        nob = True
    else:
        nob = False
    next_ok_btn2(nob)
    rgb_dis(c_c_d)
def next_ok_btn2(hover):
    font = pygame.font.SysFont(None, 50)
    if hover == False :
        pygame.draw.rect(win, (35,35,55), (1035,220,130,85))
        pygame.draw.rect(win, (35,40,60), (1040,225,120,75))
        pygame.draw.rect(win, (35,45,65), (1045,230,110,65))
        pygame.draw.rect(win, (35,50,70), (1050,235,100,55))
        pygame.draw.rect(win, (35,55,75), (1055,240,90,45))
        screen_text = font.render('Next',True,(55,80,100))
    else:
        pygame.draw.rect(win, (35,55,75), (1035,220,130,85))
        pygame.draw.rect(win, (35,50,70), (1040,225,120,75))
        pygame.draw.rect(win, (35,45,65), (1045,230,110,65))
        pygame.draw.rect(win, (35,40,60), (1050,235,100,55))
        pygame.draw.rect(win, (35,35,55), (1055,240,90,45))
        screen_text = font.render('Next',True,(15,10,35))

    win.blit(screen_text,[1062,245])
def rgb_dis(c_c_d):
    font = pygame.font.SysFont(None, 30)
    screen_text1 = font.render(str(c_c_d[0]), True, (0, 0, 0))
    screen_text2 = font.render(str(c_c_d[1]), True, (0, 0, 0))
    screen_text3 = font.render(str(c_c_d[2]), True, (0, 0, 0))
    win.blit(screen_text1,[475,253])
    win.blit(screen_text2,[555,253])
    win.blit(screen_text3,[635,253])

    pygame.draw.rect(win,c_c_d,(890,227,70,70))
def back_to_life(file):
    full=[]
    nimfull=[]
    save_file = open('save_as_file.txt','r')
    file_text = save_file.readlines(1)
    edit_file_text=file_text[0].split('>')
    edit_file_text.remove("")
    edit_file_text2 = edit_file_text[file-1].split('?')
    numbers= int(edit_file_text2[0])

    edit_file_text2.pop(0)
    for fuler in range(numbers):
        x= edit_file_text2[fuler]
        x=list(x)
        x.pop(0)

        x.pop(-1)
        for tiker in x :
            if ord(tiker)>=48 and ord(tiker)<=57:
                nimfull.append(int(tiker))
        full.append(nimfull)
        nimfull=[]
    if len(edit_file_text2) == numbers*2:
        color_type = 'c'
        for colortiker in range(numbers):
            mocolor=["","",""]
            x=0
            for ct in edit_file_text2[numbers+colortiker]:
                if ct != "'" and ct != '[' and ct !=']':
                    if ct != ',':
                        mocolor[x] += ct
                    else:
                        x +=1
            for cheng in range(3):
                mocolor[cheng]=int(mocolor[cheng])
            full.append(mocolor)
    else:
        color_type = "r"
    return [full,color_type,numbers]
def game_list(file_number):
    pygame.draw.rect(win , (0,0,10),(40,340,1125,320))
    saved = open('save_as_file.txt','r')
    sis = saved.readlines(1)
    if len(sis)>=1:
        sis3 = sis[0].split('>')
        pygame.draw.rect(win, (10, 10, 30), (340, 340, 500, 320))
        font = pygame.font.SysFont(None, 50)
        screen_text = font.render('Game number ' + str(file_number) , True, (100, 130, 160))
        win.blit(screen_text, [450, 380])
        font2 = pygame.font.SysFont(None, 40)
        ss = sis3[file_number-1][0]
        if sis3[file_number-1][1] != '?':
            ss +=sis3[file_number-1][1]
        screen_text2 = font2.render('number of shapes ' + ss , True, (100, 130, 160))
        win.blit(screen_text2, [445, 480])
def game_creater():
    save_as_filed = open('save_as_file.txt', 'a')
    save_as_filed.close()
    game_ch = True
    selected_r1 = 0
    slc_row = 1
    t_or_d = 1
    target = False
    lvl = 1
    next1 = False
    Shape_lvl = True
    color_lvl = False
    color_step = 1
    color_part = False
    c_c_d = [100,100,100]
    rand_color = True
    color_cunt = 0
    sh_list = [[], [], [], [], [], [], [], [], [], [], [], []]
    sh_list2 = [[], [], [], [], [], [], [], [], [], [], [], []]
    color_list  =[]
    write = False
    co = ''
    partcunt =[1,0]
    file = 1
    win.fill((30, 30, 50))
    if t_or_d == 1:
        sh_list[selected_r1] = obj_loct(selected_r1, target, 0, sh_list[selected_r1], t_or_d)
    else:
        sh_list2[selected_r1] = obj_loct(selected_r1, target, 0, sh_list2[selected_r1], t_or_d)
    next_ok_btn(False)

    while game_ch:
        send_event = 0
        if slc_row != 1 :
            selected_r1 =  -1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_ch = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    if partcunt[1]== 0:
                        game_ch = False
                        re = [False]

                    elif target  == False and (color_step == 1 or color_step == 5):
                        partcunt[1]=0

                if Shape_lvl == True and partcunt[1] ==1:
                    if event.key == pygame.K_RIGHT:
                        if lvl == 1 and target  == False :
                            if selected_r1 < 11 :
                                selected_r1 += 1
                    elif event.key == pygame.K_LEFT :
                        if lvl == 1 and  target == False:
                            if selected_r1 > 0 :
                                selected_r1 -= 1
                    elif event.key == pygame.K_UP:
                        if lvl == 1 and target  == False :
                            t_or_d = 1
                        if lvl == 2:
                            lvl = 1
                            next1 =False
                            t_or_d =2
                    elif event.key == pygame.K_DOWN :
                        if t_or_d == 2:
                            lvl = 2
                            next1 = True
                            t_or_d = 3
                        elif t_or_d == 1 :
                            if lvl == 1 and  target == False:
                                t_or_d = 2

                    elif event.key == pygame.K_SPACE :
                        if next1 == False and lvl == 1:
                            target = True
                        elif next1 == True and lvl == 2:
                            color_lvl = True
                            Shape_lvl = False
                            next1 = False


                    elif event.key == pygame.K_ESCAPE :
                        target = False
                    if lvl == 1:
                        if event.key == pygame.K_KP1 :
                            if target == True :
                                send_event = 7
                        elif event.key == pygame.K_KP2 :
                            if target == True :
                                send_event = 8
                        elif event.key == pygame.K_KP3 :
                            if target == True :
                                send_event = 9
                        elif event.key == pygame.K_KP4 :
                            if target == True :
                                send_event = 4
                        elif event.key == pygame.K_KP5 :
                            if target == True :
                                send_event = 5
                        elif event.key == pygame.K_KP6 :
                            if target == True :
                                send_event = 6
                        elif event.key == pygame.K_KP7 :
                            if target == True :
                                send_event = 1
                        elif event.key == pygame.K_KP8 :
                            if target == True :
                                send_event = 2
                        elif event.key == pygame.K_KP9:
                            if target == True :
                                send_event = 3
                elif color_lvl == True and partcunt[1] == 1:
                    sh_list3 = full_shape(sh_list,sh_list2)
                    if len(sh_list3) < 0:
                        color_lvl=False
                        sh_list3 =[]
                        Shape_lvl = True
                        lvl = 1
                        t_or_d = 1
                        selected_r1 = 0
                        target = False
                    else:
                        color_part=True
                        if event.key == pygame.K_SPACE:
                            if color_step == 1:
                                rand_color = not rand_color
                            elif color_step <5 and color_step>1 :
                                if color_cunt <= len(sh_list3)-1:
                                    color_list.append(c_c_d)
                                    c_c_d = [100,100,100]
                                    if color_cunt <=len(sh_list3)-1:
                                        color_cunt +=1
                            elif color_step == 5 and (rand_color == True or len(color_list) == len(sh_list3)):
                                write = True
                        elif event.key == pygame.K_ESCAPE:
                            if color_cunt >0:
                                color_cunt -=1
                                color_list.pop(-1)
                        elif event.key == pygame.K_RIGHT:
                            if rand_color == False  and color_step<=4:
                                color_step +=1
                            elif rand_color == True :
                                color_step = 5
                        elif event.key == pygame.K_LEFT :
                            if rand_color == True :
                                color_step = 1
                            elif color_step >1 :
                                color_step -= 1
                        elif event.key == pygame.K_UP:
                            if color_step == 2 and c_c_d[0]<=250:
                                c_c_d[0] += 5
                            elif color_step == 3 and c_c_d[1]<250:
                                c_c_d[1] += 5
                            elif color_step == 4 and c_c_d[2]<250:
                                c_c_d[2] += 5
                        elif event.key == pygame.K_DOWN:
                            if color_step == 2 and c_c_d[0] > 0:
                                c_c_d[0] -= 5
                            elif color_step == 3 and c_c_d[1] > 0:
                                c_c_d[1] -= 5
                            elif color_step == 4 and c_c_d[2] > 0:
                                c_c_d[2] -= 5
                if partcunt[1] == 0 :
                    if event.key == pygame.K_DOWN:
                        if partcunt[0] <2 :
                            partcunt[0]+=1
                    elif event.key == pygame.K_UP:
                        if partcunt[0]>1 :
                            partcunt[0] -=1
                    elif event.key == pygame.K_SPACE:
                        partcunt[1]= partcunt[0]

                elif partcunt[1]== 2:
                    if event.key == pygame.K_RIGHT:
                        saved = open('save_as_file.txt', 'r')
                        sis = saved.readline()
                        saved.close()

                        if len(sis.split('>'))-1 > file:
                            file += 1
                    elif event.key == pygame.K_LEFT:
                        if file>1:
                            file-=1
                    elif event.key == pygame.K_SPACE:
                        game_ch =False
                        re = [True,back_to_life(file)]
                    elif event.key == pygame.K_ESCAPE:
                        partcunt[1]=0
            if t_or_d == 1 :
                sh_list[selected_r1] = obj_loct(selected_r1,target,send_event,sh_list[selected_r1],t_or_d)
            else:
                sh_list2[selected_r1] = obj_loct(selected_r1,target,send_event,sh_list2[selected_r1],t_or_d)
            ch_box_top(sh_list)
            ch_box_top2(sh_list2)
            next_ok_btn(next1)
            if write == True :
                if rand_color == True:
                    co2=len(sh_list3)
                    sh_list3.append('r')
                    for ad in (sh_list3):
                        co += "?" +str(ad)
                else:
                    co2 = len(sh_list3)
                    for ad in (sh_list3 + color_list):
                        co += "?" + str(ad)
                save_as_file = open('save_as_file.txt','a')
                save_as_file.writelines(str(co2)+co+'>')
                selected_r1 = 0
                slc_row = 1
                t_or_d = 1
                target = False
                lvl = 1
                next1 = False
                Shape_lvl = True
                color_lvl = False
                color_step = 1
                color_part = False
                c_c_d = [100, 100, 100]
                rand_color = True
                color_cunt = 0
                sh_list = [[], [], [], [], [], [], [], [], [], [], [], []]
                sh_list2 = [[], [], [], [], [], [], [], [], [], [], [], []]
                color_list = []
                write =False
                co = ''
                game_ch = False
                re = [False]
        saved = open('save_as_file.txt', 'r')
        sis5 = saved.readlines(1)
        pygame.draw.rect(win, (0, 0, 0), (0, 0, 20, 800))

        if partcunt[1] == 0:
            pygame.draw.rect(win, (255, 125, 20), (0, (partcunt[0] - 1) * 320, 20, 320 + ((partcunt[0] - 1) * 70)))
        else:
            pygame.draw.rect(win, (255, 80, 0), (0, (partcunt[0] - 1) * 320, 20, 320 + ((partcunt[0] - 1) * 70)))

        game_list(file)
        color_tool_bar(color_part,color_step,c_c_d ,rand_color,color_cunt)
        pygame.display.update()

    win.fill((255, 255, 255))
    pygame.display.update()
    return re
Meno()
pygame.QUIT
