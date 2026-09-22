from ui import Win
from PIL import Image, ImageTk
import numpy as np
class Controller:
    
    ui: Win

    def __init__(self):
        pass

    def init(self, ui):
       
        self.ui = ui
        self.live_status = False

       
        canvas = self.ui.tk_canvas_muaz74cc
        arr = np.zeros((360, 640, 3), dtype=np.uint8)
        image = Image.fromarray(arr, "RGB")
        self.photo_resized = ImageTk.PhotoImage(image)
        self.canvas_image_id = canvas.create_image(
            0, 0, anchor="nw", image=self.photo_resized
        )
        self._after_id = None  # 

        # TODO 

    def create_image(self, evt):
        canvas = self.ui.tk_canvas_muaz74cc
        arr = np.random.randint(0, 256, (360, 640, 3), dtype=np.uint8)
        image = Image.fromarray(arr, "RGB")
        self.photo_resized = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, anchor="nw", image=self.photo_resized)

    def live_start(self, evt):
        
        if self.live_status:
            return
        self.live_status = True
        
        self.ui.tk_button_mub0ibok.config(state="disabled")
        
        self._update_frame()

    def _update_frame(self):
        
        if not self.live_status:
            return
        canvas = self.ui.tk_canvas_muaz74cc
        arr = np.random.randint(0, 256, (360, 640, 3), dtype=np.uint8)
        image = Image.fromarray(arr, "RGB")
        self.photo_resized = ImageTk.PhotoImage(image)
        
        canvas.itemconfig(self.canvas_image_id, image=self.photo_resized)
        self._after_id = canvas.after(30, self._update_frame)

    def stop_live(self, evt):
        self.live_status = False
        
        if self._after_id is not None:
            self.ui.tk_canvas_muaz74cc.after_cancel(self._after_id)
            self._after_id = None
        
        self.ui.tk_button_mub0ibok.config(state="normal")