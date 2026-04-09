def plan_path(obstacles, frame_width):
    path = "FORWARD"
    
    for (x, y, w, h) in obstacles:
        center = x + w // 2
        
        if center < frame_width // 3:
            path = "RIGHT"
        elif center > 2 * frame_width // 3:
            path = "LEFT"
        else:
            path = "STOP"
    
    return path
