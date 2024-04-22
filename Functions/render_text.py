def render_text(screen, font, x_pos, y_pos, colour, alpha, text):
  # prepares text
  label = font.render(text, 1, colour)
  label.set_alpha(alpha)
  # calculates the position
  text_width = font.size(text)[0]
  text_height = font.size(text)[1]
  # positions the text and renders
  screen.blit(label, (int(x_pos - (text_width / 2)), int(y_pos - (text_height / 2))))
