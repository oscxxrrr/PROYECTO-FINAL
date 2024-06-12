import pygame
import random
import sys

def PP_Ex3():
    # Inicializar Pygame
    pygame.init()

    # Configuración de pantalla
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PROYECTO FINAL JUEGO Ex3")

    # Cargar imagen de la bandera de España como fondo
    background_image = pygame.image.load('/home/cicles/AO/PHYTON/PROYECTO FINAL/imgs/españa.png')
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

    # Colores
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Cargar imágenes
    player_image = pygame.image.load('/home/cicles/AO/PHYTON/PROYECTO FINAL/imgs/player.png')
    enemy_image = pygame.image.load('/home/cicles/AO/PHYTON/PROYECTO FINAL/imgs/enemy.png')

    # Redimensionar imágenes
    player_size = 50
    enemy_size = 50
    player_image = pygame.transform.scale(player_image, (player_size, player_size))
    enemy_image = pygame.transform.scale(enemy_image, (enemy_size, enemy_size))

    # Configuración del jugador
    player_pos = [WIDTH // 2, HEIGHT // 2]  # Posición inicial del jugador en el centro de la pantalla
    player_speed_x = 0  # Velocidad horizontal inicial del jugador
    player_speed_y = 0  # Velocidad vertical inicial del jugador

    # Configuración del objeto
    object_pos = [random.randint(0, WIDTH - enemy_size), 0]
    object_list = [object_pos]

    # Velocidad del juego
    SPEED = 10

    # Reloj
    clock = pygame.time.Clock()

    # Puntuación
    score = 0

    # Fuente
    font = pygame.font.SysFont("monospace", 35)

    # Función para que los objetos caigan
    def drop_objects(object_list):
        # Genera un retraso aleatorio
        delay = random.random()  
        # Añade un nuevo objeto si la cantidad actual es menor que 10 y el retraso es menor que 0.1
        if len(object_list) < 10 and delay < 0.1:
            # Posición x aleatoria
            x_pos = random.randint(0, WIDTH - enemy_size)  
            # Empieza desde la parte superior de la pantalla
            y_pos = 0  
            # Añade la posición del nuevo objeto a la lista
            object_list.append([x_pos, y_pos])  

    def draw_objects(object_list):
        # Dibuja cada objeto en su posición
        for object_pos in object_list:
            screen.blit(enemy_image, (object_pos[0], object_pos[1]))  

    def update_object_positions(object_list, score):
        # Para cada objeto en la lista
        for idx, object_pos in enumerate(object_list):
            # Si el objeto está dentro de la pantalla
            if object_pos[1] >= 0 and object_pos[1] < HEIGHT:  
                # Mueve el objeto hacia abajo
                object_pos[1] += SPEED  
            else:
                # Elimina el objeto si está fuera de la pantalla
                object_list.pop(idx)  
                # Incrementa la puntuación
                score += 1  
        # Devuelve la puntuación actualizada
        return score  

    def detect_collision(player_pos, object_pos):
        p_x, p_y = player_pos
        o_x, o_y = object_pos
        # Comprueba si hay colisión entre el jugador y el objeto en términos de coordenadas
        if (o_x >= p_x and o_x < (p_x + player_size)) or (p_x >= o_x and p_x < (o_x + enemy_size)):
            if (o_y >= p_y and o_y < (p_y + player_size)) or (p_y >= o_y and p_y < (o_y + enemy_size)):
                # Devuelve True si hay colisión
                return True  
        # Devuelve False si no hay colisión
        return False  

    def check_collisions(object_list, player_pos):
        # Comprueba cada objeto en la lista
        for object_pos in object_list:
            # Si hay colisión, devuelve True
            if detect_collision(player_pos, object_pos):  
                return True  
        # Si no hay colisión, devuelve False
        return False  

    # Bucle principal del juego
    game_over = False
    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_speed_x = -10  
                elif event.key == pygame.K_RIGHT:
                    player_speed_x = 10  
                elif event.key == pygame.K_UP:
                    player_speed_y = -10  
                elif event.key == pygame.K_DOWN:
                    player_speed_y = 10  
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_speed_x = 0  
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player_speed_y = 0  

        # Actualizar la posición del jugador basada en su velocidad
        player_pos[0] += player_speed_x
        player_pos[1] += player_speed_y
        # Asegurar que el jugador no salga de los límites horizontales
        player_pos[0] = max(0, min(player_pos[0],
        WIDTH - player_size))  
        # Asegurar que el jugador no salga de los límites verticales
        player_pos[1] = max(0, min(player_pos[1], HEIGHT - player_size))  

        # Dibujar la imagen de fondo
        screen.blit(background_image, (0, 0))  

        # Dejar caer objetos
        drop_objects(object_list)  
        # Actualizar posiciones de objetos y puntuación
        score = update_object_positions(object_list, score)  

        # Verificar colisiones
        if check_collisions(object_list, player_pos):  
            game_over = True  

        # Dibujar objetos en la pantalla
        draw_objects(object_list)  

        # Dibujar jugador en la pantalla
        screen.blit(player_image, (player_pos[0], player_pos[1]))  

        # Mostrar puntuación
        text = f"Score: {score}"  
        label = font.render(text, 1, WHITE)
        screen.blit(label, (WIDTH - 200, HEIGHT - 40))  

        # Actualizar la pantalla
        pygame.display.update()  

        # Controlar la velocidad del juego
        clock.tick(30)  

    # Salir del juego
    pygame.quit()  

