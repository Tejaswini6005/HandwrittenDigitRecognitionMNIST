{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7c4641d2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1/1 [==============================] - 0s 149ms/step\n",
      "1/1 [==============================] - 0s 26ms/step\n",
      "1/1 [==============================] - 0s 30ms/step\n",
      "1/1 [==============================] - 0s 33ms/step\n",
      "1/1 [==============================] - 0s 22ms/step\n"
     ]
    }
   ],
   "source": [
    "from keras.models import load_model\n",
    "from tkinter import *\n",
    "import tkinter as tk\n",
    "import win32gui\n",
    "from PIL import ImageGrab, Image\n",
    "import numpy as np\n",
    "\n",
    "model = load_model('mnist.h5')\n",
    "\n",
    "def predict_digit(img):\n",
    "    #resize image to 28x28 pixels\n",
    "    img = img.resize((28,28))\n",
    "    #convert rgb to grayscale\n",
    "    img = img.convert('L')\n",
    "    img = np.array(img)\n",
    "    #reshaping to support our model input and normalizing\n",
    "    img = img.reshape(1,28,28,1)\n",
    "    img = img/255.0\n",
    "    #predicting the class\n",
    "    res = model.predict([img])[0]\n",
    "    return np.argmax(res), max(res)\n",
    "\n",
    "class App(tk.Tk):\n",
    "    def __init__(self):\n",
    "        tk.Tk.__init__(self)\n",
    "\n",
    "        self.x = self.y = 0\n",
    "        \n",
    "        # Creating elements\n",
    "        self.canvas = tk.Canvas(self, width=300, height=300, bg = \"white\", cursor=\"cross\")\n",
    "        self.label = tk.Label(self, text=\"Draw..\", font=(\"Helvetica\", 48))\n",
    "        self.classify_btn = tk.Button(self, text = \"Recognise\", command = self.classify_handwriting)   \n",
    "        self.button_clear = tk.Button(self, text = \"Clear\", command = self.clear_all)\n",
    "       \n",
    "        # Grid structure\n",
    "        self.canvas.grid(row=0, column=0, pady=2, sticky=W, )\n",
    "        self.label.grid(row=0, column=1,pady=2, padx=2)\n",
    "        self.classify_btn.grid(row=1, column=1, pady=2, padx=2)\n",
    "        self.button_clear.grid(row=1, column=0, pady=2)\n",
    "        \n",
    "        #self.canvas.bind(\"<Motion>\", self.start_pos)\n",
    "        self.canvas.bind(\"<B1-Motion>\", self.draw_lines)\n",
    "\n",
    "    def clear_all(self):\n",
    "        self.canvas.delete(\"all\")\n",
    "        \n",
    "    def classify_handwriting(self):\n",
    "        HWND = self.canvas.winfo_id()  # get the handle of the canvas\n",
    "        rect = win32gui.GetWindowRect(HWND)  # get the coordinate of the canvas\n",
    "        a,b,c,d = rect\n",
    "        rect=(a+4,b+4,c-4,d-4)\n",
    "        im = ImageGrab.grab(rect)\n",
    "\n",
    "        digit, acc = predict_digit(im)\n",
    "        self.label.configure(text= str(digit)+', '+ str(int(acc*100))+'%')\n",
    "\n",
    "    def draw_lines(self, event):\n",
    "        self.x = event.x\n",
    "        self.y = event.y\n",
    "        r=8\n",
    "        self.canvas.create_oval(self.x-r, self.y-r, self.x + r, self.y + r, fill='black')\n",
    "       \n",
    "app = App()\n",
    "mainloop()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "355fe258",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e51de811",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.16"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
