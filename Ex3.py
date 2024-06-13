import pygame  # Importar la biblioteca Pygame
import random  # Importar la biblioteca Random para generar números aleatorios
import sys  # Importar la biblioteca sys para salir del programa

def PP_Ex3():
    # Inicializar Pygame
    pygame.init()

    # Configuración de pantalla
    WIDTH, HEIGHT = 800, 600  # Definir el ancho y alto de la pantalla
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Crear la pantalla del juego
    pygame.display.set_caption("PROYECTO FINAL JUEGO Ex3")  # Establecer el título de la ventana del juego

    # Cargar imagen de la bandera de España como fondo
    background_image = pygame.image.load('/home/cicles/AO/PHYTON/PROYECTO FINAL/imgs/españa.png')  # Cargar la imagen de fondo
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # Escalar la imagen de fondo al tamaño de la pantalla

    # Colores
    WHITE = (255, 255, 255)  # Definir el color blanco
    BLACK = (0, 0, 0)  # Definir el color negro

    # Cargar imágenes
    player_image = pygame.image.load('/home/cicles/AO/PHYTON/PROYECTO FINAL/imgs/player.png')  # Cargar la imagen del jugador
    enemy_image = pygame.image.load('/home/cicles/AO/PHYTON/PROYECTO FINAL/imgs/enemy.png')  # Cargar la imagen del enemigo

    # Redimensionar imágenes
    player_size = 50  # Definir el tamaño del jugador
    enemy_size = 50  # Definir el tamaño del enemigo
    player_image = pygame.transform.scale(player_image, (player_size, player_size))  # Escalar la imagen del jugador
    enemy_image = pygame.transform.scale(enemy_image, (enemy_size, enemy_size))  # Escalar la imagen del enemigo

    # Configuración del jugador
    player_pos = [WIDTH // 2, HEIGHT // 2]  # Posición inicial del jugador en el centro de la pantalla
    player_speed_x = 0  # Velocidad horizontal inicial del jugador
    player_speed_y = 0  # Velocidad vertical inicial del jugador

    # Configuración del objeto
    object_pos = [random.randint(0, WIDTH - enemy_size), 0]  # Posición inicial del objeto enemigo
    object_list = [object_pos]  # Lista de objetos enemigos

    # Velocidad del juego
    SPEED = 10  # Velocidad a la que caen los objetos enemigos

    # Reloj
    clock = pygame.time.Clock()  # Crear un reloj para controlar la velocidad del juego

    # Puntuación
    score = 0  # Inicializar la puntuación

    # Fuente
    font = pygame.font.SysFont("monospace", 35)  # Definir la fuente para la puntuación

    # Función para que los objetos caigan
    def drop_objects(object_list):
        delay = random.random()  # Generar un retraso aleatorio
        if len(object_list) < 10 and delay < 0.1:  # Añadir un nuevo objeto si la cantidad actual es menor que 10 y el retraso es menor que 0.1
            x_pos = random.randint(0, WIDTH - enemy_size)  # Posición x aleatoria
            y_pos = 0  # Empieza desde la parte superior de la pantalla
            object_list.append([x_pos, y_pos])  # Añadir la posición del nuevo objeto a la lista

    def draw_objects(object_list):
        for object_pos in object_list:  # Dibujar cada objeto en su posición
            screen.blit(enemy_image, (object_pos[0], object_pos[1]))  

    def update_object_positions(object_list, score):
        for idx, object_pos in enumerate(object_list):  # Para cada objeto en la lista
            if object_pos[1] >= 0 and object_pos[1] < HEIGHT:  # Si el objeto está dentro de la pantalla
                object_pos[1] += SPEED  # Mueve el objeto hacia abajo
            else:
                object_list.pop(idx)  # Elimina el objeto si está fuera de la pantalla
                score += 1  # Incrementa la puntuación
        return score  # Devuelve la puntuación actualizada

    def detect_collision(player_pos, object_pos):
        p_x, p_y = player_pos
        o_x, o_y = object_pos
        if (o_x >= p_x and o_x < (p_x + player_size)) or (p_x >= o_x and p_x < (o_x + enemy_size)):  # Comprueba si hay colisión en términos de coordenadas x
            if (o_y >= p_y and o_y < (p_y + player_size)) or (p_y >= o_y and p_y < (o_y + enemy_size)):  # Comprueba si hay colisión en términos de coordenadas y
                return True  # Devuelve True si hay colisión
        return False  # Devuelve False si no hay colisión

    def check_collisions(object_list, player_pos):
        for object_pos in object_list:  # Comprueba cada objeto en la lista
            if detect_collision(player_pos, object_pos):  # Si hay colisión
                return True  # Devuelve True
        return False  # Si no hay colisión, devuelve False

    # Bucle principal del juego
    game_over = False
    while not game_over:
        for event in pygame.event.get():  # Iterar sobre cada evento
            if event.type == pygame.QUIT:  # Si se cierra la ventana
                sys.exit()  # Salir del programa
            if event.type == pygame.KEYDOWN:  # Si se presiona una tecla
                if event.key == pygame.K_LEFT:
                    player_speed_x = -10  # Mover a la izquierda
                elif event.key == pygame.K_RIGHT:
                    player_speed_x = 10  # Mover a la derecha
                elif event.key == pygame.K_UP:
                    player_speed_y = -10  # Mover hacia arriba
                elif event.key == pygame.K_DOWN:
                    player_speed_y = 10  # Mover hacia abajo
            if event.type == pygame.KEYUP:  # Si se suelta una tecla
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_speed_x = 0  # Detener el movimiento horizontal
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player_speed_y = 0  # Detener el movimiento vertical

        player_pos[0] += player_speed_x  # Actualizar la posición horizontal del jugador
        player_pos[1] += player_speed_y  # Actualizar la posición vertical del jugador
        player_pos[0] = max(0, min(player_pos[0], WIDTH - player_size))  # Asegurar que el jugador no salga de los límites horizontales
        player_pos[1] = max(0, min(player_pos[1], HEIGHT - player_size))  # Asegurar que el jugador no salga de los límites verticales

        screen.blit(background_image, (0, 0))  # Dibujar la imagen de fondo

        drop_objects(object_list)  # Dejar caer objetos
        score = update_object_positions(object_list, score)  # Actualizar posiciones de objetos y puntuación

        if check_collisions(object_list, player_pos):  # Verificar colisiones
            game_over = True  # Terminar el juego si hay colisión

        draw_objects(object_list)  # Dibujar objetos en la pantalla

        screen.blit(player_image, (player_pos[0], player_pos[1]))  # Dibujar jugador en la pantalla

        text = f"Score: {score}"  # Mostrar puntuación
        label = font.render(text, 1, WHITE)
        screen.blit(label, (WIDTH - 200, HEIGHT - 40))  # Mostrar la puntuación en la pantalla

        pygame.display.update()  # Actualizar la pantalla

        clock.tick(30)  # Controlar la velocidad del juego

    pygame.quit()  # Salir del juego
