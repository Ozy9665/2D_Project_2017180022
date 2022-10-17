import pico2d
import logo_state

start_state = logo_state

pico2d.open_canvas()

logo_state.enter()

while logo_state.running:
    logo_state.handle_events()
    logo_state.update()
    logo_state.draw()

logo_state.exit()

pico2d.close_canvas()