import flet as ft
import time
import asyncio





def main(page: ft.Page):
    page.window.width = 360  
    page.window.height = 800  
    page.window.resizable = False  
    page.bgcolor = "black"
    #page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    



    image_path = "MusicPlayerApp/assets\images\musicappicon.png" 
    #PLAY!
    audio_paths = [
        r"MusicPlayerApp\Bird Sounds Spectacular _ Morning Bird Sound.mp3",
        r"MusicPlayerApp\REALISTIC CAT SOUND 15MIN!!.mp3",
        r"MusicPlayerApp\Sounds That Tilt a Dogs Head  Sounds Dogs Love.mp3"
    ]
    song_names = [
        "Bird Sounds Spectacular - Morning Bird Sound",
        "Realistic Cat Sound - 15 min",
        "Sounds That Tilt a Dog's Head - Dogs Love"
    ]
    image_paths = [
        r"MusicPlayerApp\1200.jpeg",
        r"MusicPlayerApp\cat_image.jpeg",
        r"MusicPlayerApp\dog_image.jpeg"
    ]


    audio_player = ft.Audio(src=audio_paths[0], autoplay=False)
    current_track_index = 0  

  
    is_playing = False
    current_time = 0 
    total_duration = 120  

    
    current_time_text = ft.Text("0:00", color="white")
    remaining_time_text = ft.Text(f"-{int(total_duration // 60)}:{int(total_duration % 60):02}", color="white")
    progress_bar = ft.ProgressBar(value=0, width=200, color="green")
    song_name_text = ft.Text(song_names[current_track_index], size=16, weight=ft.FontWeight.BOLD, color="white") 

    def update_time():
        nonlocal current_time
        while is_playing and current_time < total_duration:
            time.sleep(1)
            current_time += 1
            minutes, seconds = divmod(current_time, 60)
            remaining_time = total_duration - current_time
            rem_minutes, rem_seconds = divmod(remaining_time, 60)
            
         
            current_time_text.value = f"{minutes}:{seconds:02}"
            remaining_time_text.value = f"-{rem_minutes}:{rem_seconds:02}"
            progress_bar.value = current_time / total_duration
            page.update()

    def play_pause_click(e):
        nonlocal is_playing, current_time
        is_playing = not is_playing
        play_pause_button.icon = ft.icons.PAUSE if is_playing else ft.icons.PLAY_ARROW

        if is_playing:
            audio_player.play()
            page.update()
            page.call_later(0, update_time)
        else:
            audio_player.pause()

        page.update()

    def previous_click(e):
        nonlocal current_track_index
        current_track_index = (current_track_index - 1) % len(audio_paths)
    
        audio_player.src = audio_paths[current_track_index]
        song_name_text.value = song_names[current_track_index] 
        album_art.src = image_paths[current_track_index]
        if is_playing:
            audio_player.play()
        else:
            audio_player.pause()
        page.update()

    def next_click(e):
        nonlocal current_track_index
        current_track_index = (current_track_index + 1) % len(audio_paths)
      
        audio_player.src = audio_paths[current_track_index]
        song_name_text.value = song_names[current_track_index] 
        album_art.src = image_paths[current_track_index]
        if is_playing:
            audio_player.play()
        else:
            audio_player.pause()
        page.update()

    def shuffle_click(e):
        shuffle_button.icon_color = "green" if shuffle_button.icon_color != "green" else "white"
        page.update()

    def repeat_click(e):
        repeat_button.icon_color = "green" if repeat_button.icon_color != "green" else "white"
        page.update()


    shuffle_button = ft.IconButton(icon=ft.icons.SHUFFLE, on_click=shuffle_click, icon_color="white")
    previous_button = ft.IconButton(icon=ft.icons.SKIP_PREVIOUS, on_click=previous_click, icon_color="white")
    play_pause_button = ft.IconButton(icon=ft.icons.PLAY_ARROW, on_click=play_pause_click, icon_color="white", icon_size=40)
    next_button = ft.IconButton(icon=ft.icons.SKIP_NEXT, on_click=next_click, icon_color="white")
    repeat_button = ft.IconButton(icon=ft.icons.REPEAT, on_click=repeat_click, icon_color="white")

 
    album_art = ft.Image(src=image_paths[0], width=250, height=250, fit=ft.ImageFit.CONTAIN)







    
    bird_sound= "assets/music/Bird Sounds Spectacular _ Morning Bird Sound.mp3"
    cat_sound = "assets/music/REALISTIC CAT SOUND 15MIN!!.mp3"
    dog_sound = "assets/music/Sounds That Tilt a Dogs Head  Sounds Dogs Love.mp3"
    


    

    #AAAAAAAalbum_screen!!!!!
    album_img = ft.Image(
        src=r"MusicPlayerApp/assets/images/cartoon-wild-animals-collection-set-2AN691H.jpg",
        width=150,
        height=150,
    )
    artist_img = ft.Image(
        src=r"MusicPlayerApp/assets/images/catpic.png",
        width=40,
        height=40,
        border_radius=ft.border_radius.all(15)
    )
    dot = ft.Image(
        src=r"MusicPlayerApp/assets/images\dot-small-svgrepo-com.svg",
        width=18,
        height=18,
        border_radius=ft.border_radius.all(15),
        color = "white"
    )
    
    
    Album_name = ft.Text("Animals Sounds",size= 20,weight=ft.FontWeight.BOLD)
    Artist_name = ft.Text("Animals",size= 15,weight=ft.FontWeight.BOLD)
    Album = ft.Text("Album",size = 10)
    Album_year=ft.Text("2024",size = 10)


    back_button = ft.IconButton(
        icon=ft.icons.ARROW_BACK,  
        icon_size=20, 
        icon_color="white",
        on_click=lambda _: page.go("/home"),  
    )                   


    play_button = ft.Container(        
            content=ft.Image(
                src=r"MusicPlayerApp/assets/images/play-button-svgrepo-com.svg",
                width=50,
                height=50,
                color = "green",                
            ),
            padding=ft.padding.only(right=10),
            on_click=lambda _: page.go("/playscreen"),
        )
    
    shuffle_button = ft.Container(        
            content=ft.Image(
                src=r"MusicPlayerApp/assets/images\shuffle-svgrepo-com.svg",
                width=40,
                height=40,
                color = "white",            
            )
        )
    
    
    three_dots_button = ft.Container(        
            content=ft.Image(
                src=r"MusicPlayerApp/assets/images/3 dot.svg",
                width=20,
                height=20,
                color = "white"
            ),
        )

    heart_button = ft.Container(        
            content=ft.Image(
                src=r"MusicPlayerApp/assets/images/heart.svg",
                width=20,
                height=20,
                color = "white"
            ),
            padding=ft.Padding(top=0, left=10, right=0, bottom=0)
        )
    
    download_button =  ft.Container(        
            content=ft.Image(
                src=r"MusicPlayerApp/assets/images\download.png",
                width=20,
                height=20,
                color = "green"
            ),
        )

    right_group  = ft.Row(
        controls=[shuffle_button,play_button],
        alignment=ft.MainAxisAlignment.END, # Align the container to the left side
        spacing=20
    )

    left_group  = ft.Row(
        controls=[heart_button, download_button , three_dots_button],
        alignment=ft.MainAxisAlignment.START, # Align the container to the left side
        spacing=20
    )

    icon_group= ft.Row(
        controls=[left_group, right_group],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )
    
    #positioning image
    album_img_container = ft.Container(
        content=album_img,
        alignment=ft.alignment.center,  # Center the image horizontally
        padding=ft.Padding(top=30, left=0, right=0, bottom=0),  # Offset from the top (100px)
    )
    artist_img_container = ft.Container(
        content=artist_img,
        alignment=ft.alignment.center,  # Center the image horizontally
        padding=ft.Padding(top=0, left=10, right=0, bottom=0),  # Offset from the top (100px)
    )           
    
    Album_name_container = ft.Container(
        content=Album_name,
        padding=ft.Padding(top=10, left=20, right=0, bottom=0),  # 20px left padding for the text container
        alignment=ft.Alignment(0, 0),  # Align the text inside the container
    )   
    Artist_name_container = ft.Container(
        content=Artist_name,
        padding=ft.Padding(top=0, left=10, right=0, bottom=0),  # 20px left padding for the text container
        alignment=ft.Alignment(0, 0),  # Align the text inside the container
    )
    Album_container = ft.Container(
        content=Album,
        padding=ft.Padding(top=0, left=15, right=0, bottom=0),  # 20px left padding for the text container
        alignment=ft.Alignment(0, 0),  # Align the text inside the container
    )
    Album_row = ft.Row(
        controls=[Album_container,dot,Album_year],
        alignment=ft.MainAxisAlignment.START,
        spacing=2
    )  
    
    Album_name_row = ft.Row(
        controls=[Album_name_container],
        alignment=ft.MainAxisAlignment.START,  # Align the container to the left side
    )  
    # Use Row to horizontally align the container (text container)
    Artist_name_img_row = ft.Row(
        controls=[artist_img_container,Artist_name_container],
        alignment=ft.MainAxisAlignment.START,  # Align the container to the left side
    )  
    
    
    #adding navigation bar
    navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.icons.HOME,
                selected_icon=ft.icons.HOME_OUTLINED,                         
                label="Home"),
            ft.NavigationBarDestination( 
                icon=ft.icons.SEARCH,
                selected_icon=ft.icons.SEARCH_OUTLINED,                        
                label="Search"),
            ft.NavigationBarDestination(
                icon=ft.icons.LIBRARY_BOOKS,
                selected_icon=ft.icons.LIBRARY_BOOKS_OUTLINED,
                label="Your Library",
            ),
        ],
    )
    #AAAAAAAalbum screen!!!!!!!


    """async def navigate_to_log_in_page():
        await asyncio.sleep(5)  # wait for 5 seconds
        page.go("/log_in")"""
    
    music_icon=ft.Image(
        src=image_path,
        fit=ft.ImageFit.COVER,
        width=100,
        height=100,
    )

    songs=ft.Text(
        "Millions of Free Songs.",
        color="white",
        size=25,
        weight="bold",
        text_align=ft.TextAlign.CENTER,
    )
    log_in_button=ft.ElevatedButton(
        "Log in",
        color="white",
        bgcolor="green",
        width=300,
        height=30,
        on_click=lambda _: page.go("/login"),
    ) 
   
    button_row = ft.Column(
        controls=[
            log_in_button
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        expand=True,
    ) 


    create_account_button=ft.ElevatedButton(
        "Create an account",
        color="white",
        bgcolor="green",
        width=200,
        height=50,
        on_click=lambda _: page.go("/home"),
    ) 
    button_account = ft.Column(
        controls=[
            create_account_button
        ],
        alignment=ft.MainAxisAlignment.END,
        expand=True,
    ) 


    b_button = ft.IconButton(
        icon=ft.icons.ARROW_BACK,  
        icon_size=20, 
        icon_color="white",
        on_click=lambda _: page.go("/album_screen"),  
    )




    #HOME PAGE!!!!
    recently_played_header = ft.Row(
        [
            ft.Text(
                "Recently played", 
                style=ft.TextThemeStyle.TITLE_MEDIUM, 
                weight=ft.FontWeight.BOLD
            ),
            ft.Row(
                [
                    ft.IconButton(icon=ft.icons.NOTIFICATIONS, tooltip="Notifications", icon_size=18),
                    ft.IconButton(icon=ft.icons.HISTORY, tooltip="Your Library", icon_size=18),
                    ft.IconButton(icon=ft.icons.SETTINGS, tooltip="Settings", icon_size=18),
                ],
                spacing=5,
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    # Recently Played Section
    recently_played_section = ft.Row(
        [
            ft.Container(
                content=ft.Column(
                        [
                            ft.Container(
                                content=ft.Image(src=r"MusicPlayerApp\assets\images\cartoon-wild-animals-collection-set-2AN691H.jpg", fit=ft.ImageFit.COVER),
                                width=70, height=70, padding=5,
                            ),
                            ft.Text("Animals Sound", size=12, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                ),
                on_click=lambda _: page.go("/album_screen"),
            ),
            ft.Column(
                [
                    ft.Container(
                        content=ft.Image(src=r"MusicPlayerApp\assets\images\image-2.png", fit=ft.ImageFit.COVER),
                        width=70, height=70, padding=5,
                    ),
                    ft.Text("Lana Del Rey", size=12, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
            ft.Column(
                [
                    ft.Container(
                        content=ft.Image(src=r"MusicPlayerApp\assets\images\image-3.png", fit=ft.ImageFit.COVER),
                        width=70, height=70, padding=5,
                    ),
                    ft.Text("Marvin Gaye", size=12, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
            ft.Column(
                [
                    ft.Container(
                        content=ft.Image(src=r"MusicPlayerApp\assets\images\image-4.png", fit=ft.ImageFit.COVER),
                        width=70, height=70, padding=5,
                    ),
                    ft.Text("Indie Pop", size=12, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=5,
    )

    # Year in Review Section
    year_in_review_section = ft.Column(
        [
            ft.Row(
                [
                    ft.Container(
                        content=ft.Image(
                            src=r"MusicPlayerApp\assets\images\image-5.png",
                            fit=ft.ImageFit.COVER,
                        ),
                        width=50, height=50, border_radius=5, padding=5,
                    ),
                    ft.Column(
                        [
                            ft.Text(
                                "#SPOTIFYWRAPPED", 
                                color=ft.colors.GREEN_ACCENT_700, 
                                size=8, 
                                weight=ft.FontWeight.BOLD
                            ),
                            ft.Text(
                                "Your 2021 in review", 
                                style=ft.TextThemeStyle.TITLE_MEDIUM, 
                                weight=ft.FontWeight.BOLD
                            ),
                        ],
                        spacing=2,
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=5,
            ),
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Container(
                                content=ft.Image(src=r"MusicPlayerApp\assets\images\image-6.png", fit=ft.ImageFit.COVER),
                                width=120, height=120, padding=5,
                            ),
                            ft.Text("Your Top Songs 2021", size=12, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                    ),
                    ft.Column(
                        [ 
                            ft.Container(
                                content=ft.Image(src=r"MusicPlayerApp/assets/images/image-7.png", fit=ft.ImageFit.COVER),
                                width=120, height=120, padding=5,
                            ),
                            ft.Text("Your Artists", size=12, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                    ),  
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=5,
            ),
        ],
        spacing=8,
    )

    # Editor's Picks Section
    editors_picks_section = ft.Column(
        [
            ft.Text(
                "Editor's picks", 
                style=ft.TextThemeStyle.TITLE_MEDIUM, 
                weight=ft.FontWeight.BOLD
            ),
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Container(
                                content=ft.Image(src=r"MusicPlayerApp\assets\images\image-8.png", fit=ft.ImageFit.COVER),
                                width=120, height=120, padding=5,
                            ),
                            ft.Text(
                                "Ed Sheeran, Big Sean, Juice WRLD, Post Malone",
                                size=10, text_align=ft.TextAlign.CENTER,
                                max_lines=2,
                                weight=ft.FontWeight.NORMAL,
                                width=120,  
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                    ),
                    ft.Column(
                        [
                            ft.Container(
                                content=ft.Image(src=r"MusicPlayerApp\assets\images\image-9.png", fit=ft.ImageFit.COVER),
                                width=120, height=120, padding=5,
                            ),
                            ft.Text(
                                "Mitski, Tame Impala, Glass Animals, Charli XCX",
                                size=10, text_align=ft.TextAlign.CENTER,
                                max_lines=2,
                                weight=ft.FontWeight.NORMAL,
                                width=120,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                    ),
                    ft.Column(
                        [
                            ft.Container(
                                content=ft.Image(src=r"MusicPlayerApp\assets\images\image-10.png", fit=ft.ImageFit.COVER),
                                width=120, height=120, padding=5,
                            ),
                            ft.Text(
                                "Rihanna, Drake, SZA, Tyler, The Creator",
                                size=10, text_align=ft.TextAlign.CENTER,
                                max_lines=2,
                                weight=ft.FontWeight.NORMAL,
                                width=120,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                    ),
                ],
                spacing=10,
            ),
        ],
        spacing=8,
    )

    # Bottom Navigation Bar
    bottom_navigation = ft.Column(
        [
            ft.Divider(height=1, thickness=2, color=ft.colors.BLUE),
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Icon(ft.icons.HOME, tooltip="Home", size=24),
                            ft.Text("Home", size=12),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Column(
                        [
                            ft.Icon(ft.icons.SEARCH, tooltip="Search", size=24),
                            ft.Text("Search", size=12),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Column(
                        [
                            ft.Icon(ft.icons.LIBRARY_MUSIC, tooltip="Library Music", size=24),
                            ft.Text("Your Library", size=12),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                spacing=30,
            ),
        ],
        spacing=5,
    )


    #HOME PAGE!!!!
    


    


    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.Container(
                            content=
                                ft.Column(
                                    controls=[
                                        ft.Container(
                                            content=music_icon,
                                            margin=ft.Margin(50, 300, 50, 50),  
                                            alignment=ft.Alignment(0,-1)
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.ElevatedButton(
                                                    "loading...",
                                                    color="white",
                                                    bgcolor="green",    
                                                    width=150,
                                                    height=30,    
                                                    on_click=lambda _: page.go("/log_in"),
                                                ),
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER,

                                        )
                                        
                                    ],
                                ),
                    ),
                ],
            ),
        )
        
        #navigate_to_log_in_page()
        #asyncio.create_task(navigate_to_log_in_page())
    



        if page.route == "/log_in":
            page.views.append(
                ft.View(
                    "/log_in",
                    [
                        ft.Container(
                            content=
                                ft.Column(
                                    controls=[
                                        ft.Container(
                                            content=songs,
                                            #bgcolor="black",
                                            margin=ft.Margin(30, 200, 30, 0),
                                        ),
                                        ft.Container(
                                            content=button_row,
                                            expand=True,
                                            margin=ft.Margin(15, 20, 0, 0), 
                                        ),                                   
                                    ],
                                ),
                        ),
                                    
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,  
                ),
                #expand=True,
            )

        if page.route == "/login":
            page.views.append(
                ft.View(
                    "/login",
                    [
                        ft.Container(
                            content=
                                ft.Column(
                                    controls=[
                                        ft.Text(
                                            "Create account",
                                            color="white",
                                            size=25,
                                            weight="bold",
                                            text_align=ft.TextAlign.CENTER,
                                        ),
                                        ft.TextField(
                                            label="What's your name?",
                                            color="white",
                                            border_color="white",
                                            text_size=20,
                                            #weight="bold",
                                            border_width=2,
                                            width=300,
                                            height=50,
                                            text_align=ft.TextAlign.LEFT,
                                        ),
                                        ft.Text(
                                            "This name will appear in your profile",
                                            color="white",
                                            size=8,
                                            weight="bold",
                                            text_align=ft.TextAlign.LEFT,
                                        ),
                                        ft.Divider(
                                            color="grey",  
                                            thickness=1,    
                                            
                                        ),
                                        ft.Text(
                                            "By tapping on Create account you agree to our Privacy Policy and Terms of use",
                                            color="white",
                                            size=10,
                                            weight="bold",
                                            text_align=ft.TextAlign.LEFT,
                                        ),
                                        ft.Container(
                                            content=button_account,
                                            expand=True,
                                            margin=ft.Margin(50, 450, 0, 60), 
                                        ),                                       
                                    ],
                                    #horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    #alignment=ft.MainAxisAlignment.START,
                                    expand=True

                                ),
                        ),
                    ],
                    #horizontal_alignment=ft.CrossAxisAlignment.END,  

                ),
            )

        if page.route == "/home":
            page.views.append(
                ft.View(
                    "/home",
                    [
                        ft.Container(
                            content=
                                ft.Column(
                                    controls=[

                                        ft.Column(
                                            [
                                                recently_played_header,
                                                ft.Container(recently_played_section, margin=ft.margin.symmetric(vertical=10)),
                                                year_in_review_section,
                                                editors_picks_section,
                                                bottom_navigation,
                                            ],
                                            spacing=15,
                                        )
                                            
                                    ],
                                ),
                        ),
                    ],
                ),
            )


        if page.route == "/album_screen":
            page.views.append(
                ft.View(
                    "/album_screen",
                    [
                        ft.Container(
                            content=
                                ft.Column(
                                    controls=[
                                        #Album_name_container,
                                        back_button,
                                        album_img_container,
                                        Album_name_row,
                                        Artist_name_img_row,
                                        Album_row,
                                        icon_group,
                                        #navigation_bar,



                                        ft.Container(
                                            content=ft.Column(
                                                [
                                                    ft.ListTile(
                                                        trailing = three_dots_button,
                                                        title=ft.Text("Bird sound"),
                                                        subtitle=ft.Text(
                                                            "Bird"
                                                        ),
                                                    ),
                                                    
                                                ]
                                            ),
                                            width=400,
                                            height=60,
                                            #on_click= play_sound1,           
                                        ),

                                        ft.Container(
                                            content=ft.Column(
                                                [
                                                    ft.ListTile(
                                                        trailing = three_dots_button,
                                                        title=ft.Text("Cat Sound"),
                                                        subtitle=ft.Text(
                                                            "Cat"
                                                        ),
                                                    ),
                                                    
                                                ]
                                            ),
                                            width=400,
                                            height=60,
                                            #on_click= play_sound2           
                                        ),

                                        ft.Container(
                                            content=ft.Column(
                                                [
                                                    ft.ListTile(
                                                        trailing = three_dots_button,
                                                        title=ft.Text("Dog Sound"),
                                                        subtitle=ft.Text(
                                                            "Dog"
                                                        ),
                                                    ),
                                                    
                                                ]
                                            ),
                                            width=400,
                                            height=60,
                                            #on_click= play_sound2           
                                        ),

                                        ft.Container(
                                            content=navigation_bar,
                                            expand=True,
                                            margin=ft.Margin(0, 40, 0, 0), 
                                        ), 
                                    ],
                                ),    
                        ),
                    ],
                    #horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )

        if page.route == "/playscreen":
            page.views.append(
                ft.View(
                    "/playscreen",
                    [
                        ft.Container(
                            content=
                                ft.Column(
                                    controls=[ 
                                        b_button,
                                        audio_player,

              
                                        album_art,
                                        song_name_text,  
                                        ft.Text("The Beatles", size=14, color="white"),

                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                current_time_text,
                                                progress_bar,
                                                remaining_time_text,
                                            ]
                                        ),

                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                shuffle_button,
                                                previous_button,
                                                play_pause_button,
                                                next_button,
                                                repeat_button,
                                            ]
                                        ),


                                    ],
                                ),
                        ),   
                    ],
                )
            )
                                       
        page.update()


    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route) 

ft.app(main)
                    
"""ft.Container(
                        
                        #bgcolor="black",
                        margin=ft.Margin(30, 200, 30, 0),
                    ))


                    ft.ElevatedButton(
                        "Log in",
                        color="white",
                        bgcolor="green",
                        width=300,
                        height=40,
                        on_click=lambda _: page.go("login"),
                        ) 
                    
                        button_row = ft.Column(
                            controls=[
                                button1
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            expand=True,
                        ) 
                            
                        page.add(ft.Container(
                        content=button_row,
                        expand=True,
                        margin=ft.Margin(0, 20, 0, 0), 
                    ))"""
