import pygame
import random
import os # Import os for path handling

pygame.init()
pygame.mixer.init() # Initialize the mixer

# --- Game Title Constant ---
GAME_TITLE = "Divyesh Yadav's Jumper Game"

# --- Screen Setup ---
S_WIDTH = 300
S_HEIGHT = 600
screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
pygame.display.set_caption(GAME_TITLE)

clock = pygame.time.Clock()
FPS = 60

# --- Game Constants ---
Gravity = 1
MAX_PLATFORM = 10
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCROLL_THRESH = 200

# --- Fonts ---
font = pygame.font.SysFont('Arial', 24)
large_font = pygame.font.SysFont('Arial', 36, bold=True)
menu_title_font = pygame.font.SysFont('Arial', 42, bold=True)


# --- Load Images and Fallbacks ---
try:
    bgIMG = pygame.image.load("Extra/Background.png").convert_alpha()
    PlayerIMG = pygame.image.load("Extra/Player-removebg-preview.png").convert_alpha()
    PlatformIMG = pygame.image.load("Extra/Platform.png").convert_alpha()
except pygame.error:
    print("Warning: Image files not found. Using fallback solid colors.")
    bgIMG = pygame.Surface((S_WIDTH, S_HEIGHT))
    bgIMG.fill(WHITE)
    PlayerIMG = pygame.Surface((45, 45))
    PlayerIMG.fill((255, 0, 0))
    PlatformIMG = pygame.Surface((60, 20))
    PlatformIMG.fill((0, 255, 0))


# --- AUDIO SETUP ---
MUSIC_FILE = "Zambolino - Way Back (freetouse.com).mp3"

try:
    # Load the music file
    pygame.mixer.music.load(MUSIC_FILE)
    pygame.mixer.music.set_volume(0.4) # Keep volume moderate (40%)
    
    # Start the music immediately and make it loop indefinitely (-1)
    pygame.mixer.music.play(-1)
except pygame.error:
    print(f"Warning: Could not load or play music file: {MUSIC_FILE}. Please ensure it is in the same directory.")
# --- END AUDIO SETUP ---


# --- Player Class ---
class Player:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(PlayerIMG, (45, 45))
        self.width = 25
        self.height = 40
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.vel_y = 0
        self.flip = False
        self.score = 0
        self.max_score = 0

    def move(self, platforms, scroll):
        dx = 0
        dy = 0
        self.rect.y += scroll

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            dx = -10
            self.flip = True
        if key[pygame.K_RIGHT]:
            dx = 10
            self.flip = False

        # Horizontal boundary
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > S_WIDTH:
            dx = S_WIDTH - self.rect.right

        # Apply gravity
        self.vel_y += Gravity
        dy += self.vel_y

        # Platform collision (only when falling)
        for platform in platforms:
            if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                if self.rect.bottom < platform.rect.centery and self.vel_y > 0:
                    dy = platform.rect.top - self.rect.bottom
                    self.vel_y = -20  # Bounce strength

        # --- GAME OVER ON GROUND TOUCH (S_HEIGHT) ---
        if self.rect.bottom + dy > S_HEIGHT:
            self.max_score = max(self.max_score, self.score)
            return True # Game Over!

        self.rect.x += dx
        self.rect.y += dy

        # Check for game over (if player falls off the top of the screen)
        if self.rect.top < 0:
            self.max_score = max(self.max_score, self.score)
            return True # Game Over

        return False

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False),
                    (self.rect.x - 12, self.rect.y - 5))

# --- Platform Class ---
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        super().__init__()
        self.image = pygame.transform.scale(PlatformIMG, (width, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, scroll):
        self.rect.y += scroll
        if self.rect.top > S_HEIGHT:
            self.kill()

# --- Helper Functions ---
def generate_platforms(platforms, num_platforms=MAX_PLATFORM):
    """Generates new platforms above the highest one until MAX_PLATFORM is reached."""
    # Initial platform at the bottom
    if not platforms:
        p = Platform(S_WIDTH // 2 - 50, S_HEIGHT - 50, 100)
        platforms.add(p)
        return

    # Find the Y-position of the highest platform
    highest_y = S_HEIGHT
    for p in platforms.sprites():
        if p.rect.y < highest_y:
            highest_y = p.rect.y

    # Generate platforms until the max count is reached
    while len(platforms) < num_platforms:
        p_w = random.randint(60, 100)
        p_x = random.randint(0, S_WIDTH - p_w)
        p_y = highest_y - random.randint(80, 120)

        p = Platform(p_x, p_y, p_w)
        platforms.add(p)
        highest_y = p_y

def draw_text(text, text_font, color, x, y):
    """Renders text to the screen."""
    text_surface = text_font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# --- Game State Management ---

def reset_game():
    """Resets all game components for a new session."""
    player.rect.center = (S_WIDTH // 2, S_HEIGHT - 100)
    player.vel_y = 0
    platform_group.empty()
    generate_platforms(platform_group)
    return False, 0, 0 # game_over, score, scroll

# --- Game Setup ---
player = Player(S_WIDTH // 2, S_HEIGHT - 100)
platform_group = pygame.sprite.Group()

# Initial state
game_over = False
menu_state = True # New state for the main menu
score = 0
scroll = 0

# --- Game Loop ---
running = True
while running:
    clock.tick(FPS)
    screen.blit(bgIMG, (0, 0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # Stop the music when the player closes the window
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()
        
        # Check for start/restart key press
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if menu_state or game_over:
                menu_state = False
                game_over, score, scroll = reset_game()

    # --- MAIN MENU STATE ---
    if menu_state:
        draw_text(GAME_TITLE, menu_title_font, BLACK, S_WIDTH // 2, S_HEIGHT // 2 - 100)
        draw_text('Press SPACE to Start', font, BLACK, S_WIDTH // 2, S_HEIGHT // 2)
        draw_text(f'Max Score: {player.max_score}', font, BLACK, S_WIDTH // 2, S_HEIGHT // 2 + 50)
        
    # --- GAME RUNNING STATE ---
    elif not game_over:
        # Scrolling logic
        if player.rect.top <= SCROLL_THRESH:
            scroll = SCROLL_THRESH - player.rect.top
            score += scroll
        else:
            scroll = 0

        # Movement and Game Over check
        game_over = player.move(platform_group, scroll)

        # Update and draw platforms
        platform_group.update(scroll)
        platform_group.draw(screen)

        # Generate new platforms
        generate_platforms(platform_group, MAX_PLATFORM)

        # Update and draw player/score
        player.score = score
        player.draw()
        draw_text(f'Score: {player.score}', font, BLACK, 50, 10)

    # --- GAME OVER STATE ---
    else:
        # Display Game Over message
        draw_text('GAME OVER', large_font, BLACK, S_WIDTH // 2, S_HEIGHT // 2 - 50)
        draw_text(f'Score: {player.score}', font, BLACK, S_WIDTH // 2, S_HEIGHT // 2)
        draw_text(f'Max Score: {player.max_score}', font, BLACK, S_WIDTH // 2, S_HEIGHT // 2 + 30)
        draw_text('Press SPACE to Restart', font, BLACK, S_WIDTH // 2, S_HEIGHT // 2 + 90)

    pygame.display.update()

# Final cleanup
pygame.quit()