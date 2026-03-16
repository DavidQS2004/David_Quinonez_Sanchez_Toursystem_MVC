import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import os
import tempfile
import math

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageTk

# =============================================================
# FUENTES
# =============================================================
_FONT_PATHS = {
    "bold": [
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
        "C:/Windows/Fonts/seguibl.ttf",
    ],
    "regular": [
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/segoeui.ttf",
    ],
}

def _get_font(style="bold", size=12):
    for path in _FONT_PATHS[style]:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return ImageFont.load_default()


# =============================================================
# PALETAS DE TEMAS
# =============================================================
THEMES = {
    "light": {
        "bg_app":        "#EEF2F7",
        "bg_form":       "#FFFFFF",
        "bg_header":     "#0D47A1",
        "fg_header":     "#FFFFFF",
        "fg_sub":        "#90CAF9",
        "bg_tab_unsel":  "#BBDEFB",
        "fg_tab_unsel":  "#0D47A1",
        "bg_tab_sel":    "#0D47A1",
        "fg_tab_sel":    "#FFFFFF",
        "bg_canvas":     "#FFFFFF",
        "border":        "#B0BEC5",
        "fg_label":      "#37474F",
        "fg_tree":       "#1A1A2E",
        "bg_tree":       "#FAFAFA",
        "bg_tree_odd":   "#F5F5F5",
        "bg_tree_even":  "#FFFFFF",
        "bg_tree_sel":   "#BBDEFB",
        "fg_tree_sel":   "#0D47A1",
        "bg_tree_head":  "#0D47A1",
        "fg_tree_head":  "#FFFFFF",
        "bg_btn_frame":  "#EEF2F7",
        "entry_fg":      "#1A1A2E",
        "entry_bg":      "#FFFFFF",
        "entry_insert":  "#1A1A2E",
        # Toggle button
        "toggle_bg":     "#263238",
        "toggle_fg":     "#FFFFFF",
        "toggle_label":  "🌙  Modo Oscuro",
    },
    "dark": {
        "bg_app":        "#1A1A2E",
        "bg_form":       "#16213E",
        "bg_header":     "#0F3460",
        "fg_header":     "#E0E0E0",
        "fg_sub":        "#7986CB",
        "bg_tab_unsel":  "#1A237E",
        "fg_tab_unsel":  "#90CAF9",
        "bg_tab_sel":    "#0F3460",
        "fg_tab_sel":    "#FFFFFF",
        "bg_canvas":     "#16213E",
        "border":        "#37474F",
        "fg_label":      "#B0BEC5",
        "fg_tree":       "#E0E0E0",
        "bg_tree":       "#1E2A3A",
        "bg_tree_odd":   "#1E2A3A",
        "bg_tree_even":  "#16213E",
        "bg_tree_sel":   "#1A237E",
        "fg_tree_sel":   "#90CAF9",
        "bg_tree_head":  "#0F3460",
        "fg_tree_head":  "#E0E0E0",
        "bg_btn_frame":  "#1A1A2E",
        "entry_fg":      "#E0E0E0",
        "entry_bg":      "#1E2A3A",
        "entry_insert":  "#90CAF9",
        # Toggle button
        "toggle_bg":     "#FDD835",
        "toggle_fg":     "#1A1A2E",
        "toggle_label":  "☀  Modo Claro",
    },
}

FONT_LABEL = ("Segoe UI", 10)
FONT_ENTRY = ("Segoe UI", 10)
FONT_BTN   = ("Segoe UI", 9, "bold")

# Colores de botones CRUD (fijo — no cambian con el tema)
BTN_COLORS = {
    "Guardar":    ("#2E7D32", "#43A047"),
    "Actualizar": ("#1565C0", "#1E88E5"),
    "Eliminar":   ("#C62828", "#E53935"),
    "Limpiar":    ("#E65100", "#FB8C00"),
    "Buscar":     ("#6A1B9A", "#8E24AA"),
    "Ver Todos":  ("#00695C", "#00897B"),
}

TAB_BANNER_COLORS = {
    "destino": "#1565C0",
    "paquete": "#2E7D32",
    "guia":    "#B71C1C",
    "cliente": "#37474F",
}


# =============================================================
# GENERADOR DE ÍCONOS PILLOW
# =============================================================
def _gradient_circle(size, color_top, color_bot):
    img  = Image.new("RGBA", (size, size), (0,0,0,0))
    grad = Image.new("RGBA", (size, size))
    for y in range(size):
        t = y / size
        r = int(color_top[0]*(1-t) + color_bot[0]*t)
        g = int(color_top[1]*(1-t) + color_bot[1]*t)
        b = int(color_top[2]*(1-t) + color_bot[2]*t)
        for x in range(size):
            grad.putpixel((x, y), (r, g, b, 255))
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse([1,1,size-2,size-2], fill=255)
    img.paste(grad, mask=mask)
    # Sombra
    shadow = Image.new("RGBA", (size+6, size+6), (0,0,0,0))
    ImageDraw.Draw(shadow).ellipse([3,4,size+3,size+4], fill=(0,0,0,50))
    shadow = shadow.filter(ImageFilter.GaussianBlur(3))
    result = Image.new("RGBA", (size+6, size+6), (0,0,0,0))
    result.alpha_composite(shadow)
    result.alpha_composite(img, (2,1))
    return result


def icon_tab_destinos():
    s=32; img=_gradient_circle(s,(66,165,245),(13,71,161))
    draw=ImageDraw.Draw(img); cx,cy=img.width//2,img.height//2; r=s//2-4
    for off in [-r//2,0,r//2]:
        draw.ellipse([cx-r+off-1,cy-2,cx+r+off+1,cy+2],outline=(255,255,255,180),width=1)
    draw.line([(cx,cy-r),(cx,cy+r)],fill=(255,255,255,180),width=1)
    draw.line([(cx-r,cy),(cx+r,cy)],fill=(255,255,255,180),width=1)
    return img

def icon_tab_paquetes():
    s=32; img=_gradient_circle(s,(102,187,106),(27,94,32))
    draw=ImageDraw.Draw(img); cx,cy=img.width//2,img.height//2
    draw.rectangle([cx-7,cy-4,cx+7,cy+7],fill=(255,255,255,200))
    draw.rectangle([cx-8,cy-8,cx+8,cy-4],fill=(255,255,255,255))
    draw.line([(cx,cy-8),(cx,cy+7)],fill=(102,187,106,255),width=2)
    draw.line([(cx-3,cy-8),(cx,cy-5),(cx+3,cy-8)],fill=(102,187,106,255),width=1)
    return img

def icon_tab_guias():
    s=32; img=_gradient_circle(s,(239,83,80),(183,28,28))
    draw=ImageDraw.Draw(img); cx,cy=img.width//2,img.height//2
    draw.ellipse([cx-4,cy-10,cx+4,cy-3],fill=(255,255,255,230))
    draw.polygon([(cx-7,cy+9),(cx+7,cy+9),(cx+5,cy-1),(cx-5,cy-1)],fill=(255,255,255,200))
    return img

def icon_tab_clientes():
    s=32; img=_gradient_circle(s,(120,144,156),(38,50,56))
    draw=ImageDraw.Draw(img); cx,cy=img.width//2,img.height//2
    draw.ellipse([cx-1,cy-11,cx+6,cy-5],fill=(255,255,255,150))
    draw.polygon([(cx-1,cy+9),(cx+9,cy+9),(cx+8,cy-2),(cx,cy-2)],fill=(255,255,255,130))
    draw.ellipse([cx-7,cy-9,cx+1,cy-3],fill=(255,255,255,230))
    draw.polygon([(cx-9,cy+9),(cx+3,cy+9),(cx+2,cy-1),(cx-8,cy-1)],fill=(255,255,255,210))
    return img

def icon_btn_save():
    s=24; img=_gradient_circle(s,(102,187,106),(27,94,32))
    draw=ImageDraw.Draw(img); cx,cy=img.width//2,img.height//2
    draw.rectangle([cx-6,cy-6,cx+6,cy+6],fill=(255,255,255,220))
    draw.rectangle([cx-4,cy-6,cx+4,cy-1],fill=(144,202,249,255))
    draw.rectangle([cx-1,cy-6,cx+3,cy-2],fill=(200,200,200,255))
    return img

def icon_btn_update():
    s=24; img=_gradient_circle(s,(79,195,247),(13,71,161))
    draw=ImageDraw.Draw(img); cx,cy=img.width//2,img.height//2; r=6
    pts=[]
    for a in range(30,330,15):
        rad=math.radians(a)
        pts.append((cx+r*math.cos(rad),cy+r*math.sin(rad)))
    for i in range(len(pts)-1):
        draw.line([pts[i],pts[i+1]],fill=(255,255,255,230),width=2)
    draw.polygon([(cx+r-1,cy-4),(cx+r+3,cy-1),(cx+r-1,cy+2)],fill=(255,255,255,255))
    return img

def icon_btn_delete():
    s=24; img=_gradient_circle(s,(239,83,80),(183,28,28))
    draw=ImageDraw.Draw(img); cx,cy=img.width//2,img.height//2
    draw.rectangle([cx-6,cy-7,cx+6,cy-5],fill=(255,255,255,230))
    draw.rectangle([cx-3,cy-9,cx+3,cy-7],fill=(255,255,255,180))
    draw.rectangle([cx-5,cy-5,cx+5,cy+6],fill=(255,255,255,200))
    for lx in [cx-2,cx+1]:
        draw.line([(lx,cy-3),(lx,cy+4)],fill=(239,83,80,200),width=1)
    return img

def icon_btn_clear():
    s=24; img=_gradient_circle(s,(255,183,77),(230,81,0))
    draw=ImageDraw.Draw(img); cx,cy=img.width//2,img.height//2
    draw.line([(cx-5,cy-7),(cx+5,cy+5)],fill=(255,255,255,230),width=2)
    draw.polygon([(cx+2,cy+2),(cx+7,cy+4),(cx+5,cy+8),(cx,cy+6)],fill=(255,255,255,210))
    return img

def icon_btn_search():
    s=24; img=_gradient_circle(s,(186,104,200),(106,27,154))
    draw=ImageDraw.Draw(img); cx,cy=img.width//2,img.height//2
    draw.ellipse([cx-7,cy-7,cx+1,cy+1],outline=(255,255,255,230),width=2)
    draw.line([(cx+1,cy+1),(cx+6,cy+6)],fill=(255,255,255,230),width=2)
    return img

def icon_btn_showall():
    s=24; img=_gradient_circle(s,(77,208,225),(0,96,100))
    draw=ImageDraw.Draw(img); cx,cy=img.width//2,img.height//2
    for ry in [cy-5,cy,cy+5]:
        draw.rectangle([cx-6,ry-1,cx+6,ry+1],fill=(255,255,255,220))
    draw.line([(cx-1,cy-7),(cx-1,cy+7)],fill=(255,255,255,120),width=1)
    return img

def icon_favicon():
    s=48; img=_gradient_circle(s,(66,165,245),(13,71,161))
    draw=ImageDraw.Draw(img); cx,cy=img.width//2,img.height//2
    draw.polygon([(cx-14,cy+5),(cx+14,cy),(cx-14,cy-5)],fill=(255,255,255,240))
    draw.polygon([(cx-6,cy-4),(cx+2,cy-1),(cx-4,cy-12)],fill=(255,255,255,210))
    draw.polygon([(cx-6,cy+4),(cx+2,cy+1),(cx-4,cy+12)],fill=(255,255,255,180))
    draw.line([(cx-12,cy-2),(cx+10,cy)],fill=(200,232,255,160),width=1)
    return img

def icon_theme_moon():
    """Luna para botón 'Modo Oscuro'."""
    s=24; img=_gradient_circle(s,(38,50,56),(21,27,31))
    draw=ImageDraw.Draw(img); cx,cy=img.width//2,img.height//2
    draw.ellipse([cx-6,cy-6,cx+6,cy+6],fill=(255,255,200,230))
    draw.ellipse([cx-1,cy-7,cx+7,cy+1],fill=(38,50,56,255))
    return img

def icon_theme_sun():
    """Sol para botón 'Modo Claro'."""
    s=24; img=_gradient_circle(s,(255,214,0),(255,160,0))
    draw=ImageDraw.Draw(img); cx,cy=img.width//2,img.height//2
    draw.ellipse([cx-5,cy-5,cx+5,cy+5],fill=(255,255,255,240))
    for a in range(0,360,45):
        rad=math.radians(a)
        x1=cx+7*math.cos(rad); y1=cy+7*math.sin(rad)
        x2=cx+9*math.cos(rad); y2=cy+9*math.sin(rad)
        draw.line([(x1,y1),(x2,y2)],fill=(255,255,255,200),width=2)
    return img


# =============================================================
# CLASE DE CONEXIÓN
# =============================================================
class DatabaseConnector:
    def __init__(self, host, user, password, database):
        self.host=host; self.user=user
        self.password=password; self.database=database
        self.connection=None; self.cursor=None

    def connect(self):
        try:
            self.connection=mysql.connector.connect(
                host=self.host,user=self.user,
                password=self.password,database=self.database)
            self.cursor=self.connection.cursor()
        except mysql.connector.Error as e:
            messagebox.showerror("Error de conexión",str(e))

    def disconnect(self):
        if self.connection: self.connection.close()

    def execute_procedure(self,proc,*args):
        try:
            self.cursor.callproc(proc,args)
            results=[]
            for r in self.cursor.stored_results():
                rows=r.fetchall()
                if rows:
                    headers=[i[0] for i in r.description]
                    results.append((headers,rows))
            self.connection.commit()
            return results
        except mysql.connector.Error as e:
            self.connection.rollback()
            messagebox.showerror("Error SQL",f"{proc}:\n{e}")
            return None


# =============================================================
# APLICACIÓN PRINCIPAL
# =============================================================
class DestinosSonadosApp(tk.Tk):
    def __init__(self, db: DatabaseConnector):
        super().__init__()
        self.db = db
        self._current_theme = "light"   # Estado inicial

        # Registro de todos los widgets temizables
        self._themed_widgets = []       # lista de (widget, rol)
        self._themed_trees   = []       # Treeviews
        self._themed_canvases = []      # Canvas de formularios
        self._themed_forms   = []       # tk.Frame de formularios
        self._themed_entries = []       # ttk.Entry

        self.title("DESTINO SOÑADO S.A.")
        self.geometry("1060x760")
        self.minsize(920, 660)

        self._load_icons()
        self._set_favicon()
        self._apply_ttk_styles()
        self._build_header()
        self._build_notebook()
        self._apply_theme()             # Pintar todo con el tema inicial

    # ─────────────────────────────────────────────────────────
    # ÍCONOS
    # ─────────────────────────────────────────────────────────
    def _load_icons(self):
        fns = {
            "destino":    icon_tab_destinos,
            "paquete":    icon_tab_paquetes,
            "guia":       icon_tab_guias,
            "cliente":    icon_tab_clientes,
            "Guardar":    icon_btn_save,
            "Actualizar": icon_btn_update,
            "Eliminar":   icon_btn_delete,
            "Limpiar":    icon_btn_clear,
            "Buscar":     icon_btn_search,
            "Ver Todos":  icon_btn_showall,
            "moon":       icon_theme_moon,
            "sun":        icon_theme_sun,
        }
        self.ico = {k: ImageTk.PhotoImage(fn()) for k, fn in fns.items()}

    def _set_favicon(self):
        pil = icon_favicon().resize((48,48), Image.LANCZOS)
        tmp = tempfile.NamedTemporaryFile(suffix=".ico", delete=False)
        self._favicon_tmp = tmp.name; tmp.close()
        try:
            pil.save(self._favicon_tmp, format="ICO",
                     sizes=[(16,16),(32,32),(48,48)],
                     append_images=[pil.resize((16,16),Image.LANCZOS),
                                    pil.resize((32,32),Image.LANCZOS)])
            self.iconbitmap(self._favicon_tmp)
        except Exception:
            self._favicon_tk = ImageTk.PhotoImage(pil)
            self.iconphoto(True, self._favicon_tk)
        self.protocol("WM_DELETE_WINDOW", self._on_close)

    def _on_close(self):
        try:
            if os.path.exists(self._favicon_tmp):
                os.unlink(self._favicon_tmp)
        except Exception: pass
        self.destroy()

    # ─────────────────────────────────────────────────────────
    # ESTILOS TTK (se regeneran al cambiar tema)
    # ─────────────────────────────────────────────────────────
    def _apply_ttk_styles(self):
        t  = THEMES[self._current_theme]
        s  = ttk.Style(self)
        s.theme_use("clam")
        s.configure("TNotebook",
                    background=t["bg_app"], borderwidth=0,
                    tabmargins=[2,5,0,0])
        s.configure("TNotebook.Tab",
                    font=("Segoe UI",10,"bold"),
                    padding=[14,8],
                    background=t["bg_tab_unsel"],
                    foreground=t["fg_tab_unsel"])
        s.map("TNotebook.Tab",
              background=[("selected",t["bg_tab_sel"])],
              foreground=[("selected",t["fg_tab_sel"])])
        s.configure("TFrame",  background=t["bg_app"])
        s.configure("TLabel",  background=t["bg_form"], font=FONT_LABEL)
        s.configure("TEntry",
                    font=FONT_ENTRY, padding=4,
                    fieldbackground=t["entry_bg"],
                    foreground=t["entry_fg"],
                    insertcolor=t["entry_insert"])
        s.configure("Vertical.TScrollbar",
                    background=t["bg_app"],
                    troughcolor=t["bg_form"],
                    arrowcolor=t["fg_label"])
        s.configure("Horizontal.TScrollbar",
                    background=t["bg_app"],
                    troughcolor=t["bg_form"],
                    arrowcolor=t["fg_label"])
        s.configure("Treeview",
                    font=("Segoe UI",9), rowheight=25,
                    background=t["bg_tree"],
                    fieldbackground=t["bg_tree"],
                    foreground=t["fg_tree"])
        s.configure("Treeview.Heading",
                    font=("Segoe UI",9,"bold"),
                    background=t["bg_tree_head"],
                    foreground=t["fg_tree_head"],
                    relief="flat")
        s.map("Treeview",
              background=[("selected",t["bg_tree_sel"])],
              foreground=[("selected",t["fg_tree_sel"])])

    # ─────────────────────────────────────────────────────────
    # APLICAR TEMA A WIDGETS
    # ─────────────────────────────────────────────────────────
    def _apply_theme(self):
        t = THEMES[self._current_theme]
        self.configure(bg=t["bg_app"])
        self._apply_ttk_styles()

        for widget, role in self._themed_widgets:
            try:
                if role == "bg_app":
                    widget.configure(bg=t["bg_app"])
                elif role == "bg_form":
                    widget.configure(bg=t["bg_form"])
                elif role == "bg_header":
                    widget.configure(bg=t["bg_header"])
                elif role == "fg_header":
                    widget.configure(bg=t["bg_header"], fg=t["fg_header"])
                elif role == "fg_sub":
                    widget.configure(bg=t["bg_header"], fg=t["fg_sub"])
                elif role == "fg_label":
                    widget.configure(bg=t["bg_form"], fg=t["fg_label"])
                elif role == "btn_frame":
                    widget.configure(bg=t["bg_btn_frame"])
            except Exception:
                pass

        # Canvas de formularios
        for canvas, form in self._themed_canvases:
            try:
                canvas.configure(bg=t["bg_canvas"],
                                 highlightbackground=t["border"])
                form.configure(bg=t["bg_form"])
                # Actualizar todos los Label dentro del form
                for child in form.winfo_children():
                    if isinstance(child, tk.Label):
                        child.configure(bg=t["bg_form"], fg=t["fg_label"])
            except Exception:
                pass

        # Treeviews
        for tree in self._themed_trees:
            try:
                tree.tag_configure("odd",  background=t["bg_tree_odd"])
                tree.tag_configure("even", background=t["bg_tree_even"])
                # Repintar el Frame contenedor
                tree.master.configure(bg=t["bg_app"])
            except Exception:
                pass

        # Botón de tema
        if hasattr(self, "_theme_btn"):
            ico_key = "sun" if self._current_theme == "dark" else "moon"
            self._theme_btn.configure(
                bg=t["toggle_bg"],
                fg=t["toggle_fg"],
                activebackground=t["toggle_bg"],
                activeforeground=t["toggle_fg"],
                text=f"  {t['toggle_label']}",
                image=self.ico[ico_key])

        # Header
        if hasattr(self, "_hdr_frame"):
            self._hdr_frame.configure(bg=t["bg_header"])

    def _toggle_theme(self):
        self._current_theme = "dark" if self._current_theme == "light" else "light"
        self._apply_theme()

    # ─────────────────────────────────────────────────────────
    # ENCABEZADO
    # ─────────────────────────────────────────────────────────
    def _build_header(self):
        t = THEMES[self._current_theme]
        hdr = tk.Frame(self, bg=t["bg_header"], height=62)
        hdr.pack(fill="x")
        hdr.pack_propagate(False)
        self._hdr_frame = hdr
        self._themed_widgets.append((hdr, "bg_header"))

        # Logo
        logo_pil = icon_favicon().resize((42,42), Image.LANCZOS)
        self._logo_tk = ImageTk.PhotoImage(logo_pil)
        tk.Label(hdr, image=self._logo_tk,
                 bg=t["bg_header"]).pack(side="left", padx=14, pady=10)

        # Títulos
        title_frame = tk.Frame(hdr, bg=t["bg_header"])
        title_frame.pack(side="left")
        self._themed_widgets.append((title_frame, "bg_header"))

        lbl_title = tk.Label(title_frame,
                             text="DESTINOS SOÑADOS S.A.",
                             font=("Segoe UI",15,"bold"),
                             bg=t["bg_header"], fg=t["fg_header"])
        lbl_title.pack(anchor="w")
        self._themed_widgets.append((lbl_title, "fg_header"))

        lbl_sub = tk.Label(title_frame,
                           text="Sistema de Administración Turística",
                           font=("Segoe UI",9,"italic"),
                           bg=t["bg_header"], fg=t["fg_sub"])
        lbl_sub.pack(anchor="w")
        self._themed_widgets.append((lbl_sub, "fg_sub"))

        # ── BOTÓN TOGGLE TEMA ──────────────────────────────
        self._theme_btn = tk.Button(
            hdr,
            text=f"  {t['toggle_label']}",
            command=self._toggle_theme,
            font=("Segoe UI", 9, "bold"),
            bg=t["toggle_bg"], fg=t["toggle_fg"],
            activebackground=t["toggle_bg"],
            activeforeground=t["toggle_fg"],
            relief="flat", padx=12, pady=6,
            cursor="hand2",
            image=self.ico["moon"],
            compound="left", bd=0,
            borderwidth=0)
        self._theme_btn.pack(side="right", padx=16, pady=12)

    # ─────────────────────────────────────────────────────────
    # NOTEBOOK
    # ─────────────────────────────────────────────────────────
    def _build_notebook(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both", padx=8, pady=8)
        tabs = [
            ("tab_dest", "  Destinos",            "destino"),
            ("tab_paq",  "  Paquetes Turísticos",  "paquete"),
            ("tab_guia", "  Gestión Guías",        "guia"),
            ("tab_cli",  "  Gestión Clientes",     "cliente"),
        ]
        for attr, label, ico_key in tabs:
            frame = ttk.Frame(self.notebook)
            setattr(self, attr, frame)
            self.notebook.add(frame, text=label,
                              image=self.ico[ico_key], compound="left")
        self._build_tab_destinos()
        self._build_tab_paquetes()
        self._build_tab_guias()
        self._build_tab_clientes()

    # ─────────────────────────────────────────────────────────
    # HELPERS
    # ─────────────────────────────────────────────────────────
    def _banner(self, parent, text, bg, ico_key):
        bar = tk.Frame(parent, bg=bg, height=40)
        bar.pack(fill="x")
        bar.pack_propagate(False)
        tk.Label(bar, image=self.ico[ico_key],
                 bg=bg, padx=4).pack(side="left", padx=10)
        tk.Label(bar, text=text,
                 font=("Segoe UI",12,"bold"),
                 bg=bg, fg="white").pack(side="left")
        # No se agrega a _themed_widgets: los banners mantienen
        # su color de acento independiente del tema.

    def _scrollable_form(self, parent):
        t = THEMES[self._current_theme]
        wrapper = tk.Frame(parent, bg=t["bg_app"])
        wrapper.pack(fill="x", padx=8, pady=4)
        self._themed_widgets.append((wrapper, "bg_app"))

        canvas = tk.Canvas(wrapper, bg=t["bg_canvas"], height=296,
                           highlightthickness=1,
                           highlightbackground=t["border"])
        sb = ttk.Scrollbar(wrapper, orient="vertical", command=canvas.yview)
        form = tk.Frame(canvas, bg=t["bg_form"])
        form.bind("<Configure>",
                  lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0,0), window=form, anchor="nw")
        canvas.configure(yscrollcommand=sb.set)
        canvas.pack(side="left", fill="x", expand=True)
        sb.pack(side="right", fill="y")
        canvas.bind_all("<MouseWheel>",
                        lambda e: canvas.yview_scroll(
                            int(-1*(e.delta/120)), "units"))
        self._themed_canvases.append((canvas, form))
        return form

    def _field(self, form, row, label, key, store):
        t = THEMES[self._current_theme]
        lbl = tk.Label(form, text=label, font=FONT_LABEL,
                       bg=t["bg_form"], fg=t["fg_label"],
                       anchor="w", width=28)
        lbl.grid(row=row, column=0, sticky="w", padx=(18,6), pady=5)
        ent = ttk.Entry(form, width=40, font=FONT_ENTRY)
        ent.grid(row=row, column=1, sticky="w", pady=5, padx=(0,18))
        store[key] = ent
        self._themed_entries.append(ent)

    def _buttons(self, parent, callbacks):
        t = THEMES[self._current_theme]
        frm = tk.Frame(parent, bg=t["bg_btn_frame"], pady=8)
        frm.pack()
        self._themed_widgets.append((frm, "btn_frame"))
        for label, cmd in callbacks.items():
            dark, light = BTN_COLORS.get(label, ("#455A64","#607D8B"))
            ico = self.ico.get(label)
            btn = tk.Button(
                frm, text=f"  {label}", command=cmd,
                font=FONT_BTN, bg=dark, fg="white",
                activebackground=light, activeforeground="white",
                relief="flat", padx=10, pady=6,
                cursor="hand2", image=ico, compound="left", bd=0)
            btn.pack(side="left", padx=4)
            btn.bind("<Enter>", lambda e, b=btn, c=light: b.config(bg=c))
            btn.bind("<Leave>", lambda e, b=btn, c=dark:  b.config(bg=c))

    def _make_tree(self, parent):
        t = THEMES[self._current_theme]
        frm = tk.Frame(parent, bg=t["bg_app"])
        frm.pack(fill="both", expand=True, padx=8, pady=(2,8))
        self._themed_widgets.append((frm, "bg_app"))
        tree = ttk.Treeview(frm, show="headings", height=9)
        vsb  = ttk.Scrollbar(frm, orient="vertical",   command=tree.yview)
        hsb  = ttk.Scrollbar(frm, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        vsb.pack(side="right",  fill="y")
        hsb.pack(side="bottom", fill="x")
        tree.pack(fill="both",  expand=True)
        tree.tag_configure("odd",  background=t["bg_tree_odd"])
        tree.tag_configure("even", background=t["bg_tree_even"])
        self._themed_trees.append(tree)
        return tree

    def _populate(self, tree, results):
        tree.delete(*tree.get_children())
        if not results: return
        headers, rows = results[0]
        tree["columns"] = headers
        for col in headers:
            tree.heading(col, text=col)
            tree.column(col, width=118, anchor="w", stretch=True)
        for i, row in enumerate(rows):
            tree.insert("","end", values=row,
                        tags=("even" if i%2==0 else "odd",))

    def _clear(self, store):
        for e in store.values(): e.delete(0, tk.END)

    def _req_id(self, store, key, nombre):
        v = store[key].get().strip()
        if not v:
            messagebox.showwarning("Campo requerido",
                                   f"Ingrese el {nombre} para continuar.")
        return v

    def _load_row(self, tree, store, keys):
        sel = tree.selection()
        if not sel: return
        vals = tree.item(sel[0], "values")
        self._clear(store)
        for k, v in zip(keys, vals):
            if v and v != "None":
                store[k].insert(0, v)

    # ==========================================================
    # PESTAÑA 1 — DESTINOS
    # ==========================================================
    def _build_tab_destinos(self):
        self._banner(self.tab_dest,
                     "Registro de Destinos Turísticos",
                     TAB_BANNER_COLORS["destino"], "destino")
        form = self._scrollable_form(self.tab_dest)
        self.e_dest = {}
        CAMPOS = [
            ("ID Destino:",               "IDDestino"),
            ("Nombre del destino:",       "Nombre"),
            ("País:",                     "Pais"),
            ("Región:",                   "Region"),
            ("Coordenadas geográficas:",  "Coordenadas"),
            ("Tipo de destino:",          "Tipo"),
            ("Descripción:",              "Descripcion"),
            ("Temporadas recomendadas:",  "Temporadas"),
            ("Nivel de popularidad:",     "Popularidad"),
            ("Restricciones conocidas:",  "Restricciones"),
            ("Fotografías (URLs):",       "Fotografias"),
        ]
        for i,(lbl,key) in enumerate(CAMPOS): self._field(form,i,lbl,key,self.e_dest)
        self._buttons(self.tab_dest,{
            "Guardar":    self._dest_insert,
            "Actualizar": self._dest_update,
            "Eliminar":   self._dest_delete,
            "Limpiar":    lambda: self._clear(self.e_dest),
            "Buscar":     self._dest_search,
            "Ver Todos":  self._dest_all,
        })
        self.tree_dest = self._make_tree(self.tab_dest)
        KEYS = [c[1] for c in CAMPOS]
        self.tree_dest.bind("<<TreeviewSelect>>",
            lambda e: self._load_row(self.tree_dest,self.e_dest,KEYS))

    def _dest_insert(self):
        e=self.e_dest
        r=self.db.execute_procedure('sp_InsertDestino',
            e["Nombre"].get(),e["Pais"].get(),e["Region"].get(),
            e["Coordenadas"].get(),e["Tipo"].get(),e["Descripcion"].get(),
            e["Temporadas"].get(),e["Popularidad"].get() or None,
            e["Restricciones"].get(),e["Fotografias"].get())
        if r is not None:
            messagebox.showinfo("✔ Guardado","Destino guardado correctamente.")
            self._clear(self.e_dest); self._dest_all()

    def _dest_update(self):
        id_=self._req_id(self.e_dest,"IDDestino","IDDestino")
        if not id_: return
        e=self.e_dest
        r=self.db.execute_procedure('sp_UpdateDestino',id_,
            e["Nombre"].get(),e["Pais"].get(),e["Region"].get(),
            e["Coordenadas"].get(),e["Tipo"].get(),e["Descripcion"].get(),
            e["Temporadas"].get(),e["Popularidad"].get() or None,
            e["Restricciones"].get(),e["Fotografias"].get())
        if r is not None:
            messagebox.showinfo("✔ Actualizado","Destino actualizado.")
            self._dest_all()

    def _dest_delete(self):
        id_=self._req_id(self.e_dest,"IDDestino","IDDestino")
        if not id_: return
        if messagebox.askyesno("Confirmar","¿Eliminar este destino?"):
            r=self.db.execute_procedure('sp_DeleteDestino',id_)
            if r is not None:
                messagebox.showinfo("✔ Eliminado","Destino eliminado.")
                self._clear(self.e_dest); self._dest_all()

    def _dest_search(self):
        id_=self._req_id(self.e_dest,"IDDestino","IDDestino")
        if not id_: return
        r=self.db.execute_procedure('sp_GetDestino',id_)
        if r: self._populate(self.tree_dest,r)
        else: messagebox.showinfo("Sin resultados","Destino no encontrado.")

    def _dest_all(self):
        self._populate(self.tree_dest,self.db.execute_procedure('sp_GetAllDestinos'))

    # ==========================================================
    # PESTAÑA 2 — PAQUETES
    # ==========================================================
    def _build_tab_paquetes(self):
        self._banner(self.tab_paq,
                     "Gestión de Paquetes Turísticos",
                     TAB_BANNER_COLORS["paquete"], "paquete")
        form = self._scrollable_form(self.tab_paq)
        self.e_paq = {}
        CAMPOS = [
            ("ID Paquete:",              "IDPaquete"),
            ("Nombre comercial:",        "NombreComercial"),
            ("Destinos incluidos:",      "DestinosIncluidos"),
            ("Duración (días):",         "DuracionDias"),
            ("Duración (noches):",       "DuracionNoches"),
            ("Transporte:",              "Transporte"),
            ("Categoría alojamiento:",   "Alojamiento"),
            ("Régimen alimenticio:",     "Alimentacion"),
            ("Actividades incluidas:",   "ActIncluidas"),
            ("Actividades opcionales:",  "ActOpcionales"),
            ("Precio base:",             "PrecioBase"),
            ("Temporadas disponibles:",  "Temporadas"),
            ("Mínimo participantes:",    "MinimoParticipantes"),
            ("Nivel de dificultad:",     "Dificultad"),
        ]
        for i,(lbl,key) in enumerate(CAMPOS): self._field(form,i,lbl,key,self.e_paq)
        self._buttons(self.tab_paq,{
            "Guardar":    self._paq_insert,
            "Actualizar": self._paq_update,
            "Eliminar":   self._paq_delete,
            "Limpiar":    lambda: self._clear(self.e_paq),
            "Buscar":     self._paq_search,
            "Ver Todos":  self._paq_all,
        })
        self.tree_paq = self._make_tree(self.tab_paq)
        KEYS = [c[1] for c in CAMPOS]
        self.tree_paq.bind("<<TreeviewSelect>>",
            lambda e: self._load_row(self.tree_paq,self.e_paq,KEYS))

    def _paq_insert(self):
        e=self.e_paq
        r=self.db.execute_procedure('sp_InsertPaquete',
            e["NombreComercial"].get(),e["DestinosIncluidos"].get(),
            e["DuracionDias"].get() or None,e["DuracionNoches"].get() or None,
            e["Transporte"].get(),e["Alojamiento"].get(),
            e["Alimentacion"].get(),e["ActIncluidas"].get(),
            e["ActOpcionales"].get(),e["PrecioBase"].get() or None,
            e["Temporadas"].get(),e["MinimoParticipantes"].get() or None,
            e["Dificultad"].get())
        if r is not None:
            messagebox.showinfo("✔ Guardado","Paquete guardado.")
            self._clear(self.e_paq); self._paq_all()

    def _paq_update(self):
        id_=self._req_id(self.e_paq,"IDPaquete","IDPaquete")
        if not id_: return
        e=self.e_paq
        r=self.db.execute_procedure('sp_UpdatePaquete',id_,
            e["NombreComercial"].get(),e["DestinosIncluidos"].get(),
            e["DuracionDias"].get() or None,e["DuracionNoches"].get() or None,
            e["Transporte"].get(),e["Alojamiento"].get(),
            e["Alimentacion"].get(),e["ActIncluidas"].get(),
            e["ActOpcionales"].get(),e["PrecioBase"].get() or None,
            e["Temporadas"].get(),e["MinimoParticipantes"].get() or None,
            e["Dificultad"].get())
        if r is not None:
            messagebox.showinfo("✔ Actualizado","Paquete actualizado.")
            self._paq_all()

    def _paq_delete(self):
        id_=self._req_id(self.e_paq,"IDPaquete","IDPaquete")
        if not id_: return
        if messagebox.askyesno("Confirmar","¿Eliminar este paquete?"):
            r=self.db.execute_procedure('sp_DeletePaquete',id_)
            if r is not None:
                messagebox.showinfo("✔ Eliminado","Paquete eliminado.")
                self._clear(self.e_paq); self._paq_all()

    def _paq_search(self):
        id_=self._req_id(self.e_paq,"IDPaquete","IDPaquete")
        if not id_: return
        r=self.db.execute_procedure('sp_GetPaquete',id_)
        if r: self._populate(self.tree_paq,r)
        else: messagebox.showinfo("Sin resultados","Paquete no encontrado.")

    def _paq_all(self):
        self._populate(self.tree_paq,self.db.execute_procedure('sp_GetAllPaquetes'))

    # ==========================================================
    # PESTAÑA 3 — GUÍAS
    # ==========================================================
    def _build_tab_guias(self):
        self._banner(self.tab_guia,
                     "Gestión de Guías Turísticos",
                     TAB_BANNER_COLORS["guia"], "guia")
        form = self._scrollable_form(self.tab_guia)
        self.e_guia = {}
        CAMPOS = [
            ("ID Guía:",                  "IDGuia"),
            ("Nombres:",                  "Nombres"),
            ("Apellidos:",                "Apellidos"),
            ("Documento:",                "Documento"),
            ("Fecha de nacimiento:",      "FechaNacimiento"),
            ("Nacionalidad:",             "Nacionalidad"),
            ("Idiomas que habla:",        "Idiomas"),
            ("Especialidades:",           "Especialidades"),
            ("Destinos que conoce:",      "Destinos"),
            ("Certificaciones:",          "Certificaciones"),
            ("Evaluación desempeño:",     "Desempeño"),
            ("Disponibilidad:",           "Disponibilidad"),
        ]
        for i,(lbl,key) in enumerate(CAMPOS): self._field(form,i,lbl,key,self.e_guia)
        self._buttons(self.tab_guia,{
            "Guardar":    self._guia_insert,
            "Actualizar": self._guia_update,
            "Eliminar":   self._guia_delete,
            "Limpiar":    lambda: self._clear(self.e_guia),
            "Buscar":     self._guia_search,
            "Ver Todos":  self._guia_all,
        })
        self.tree_guia = self._make_tree(self.tab_guia)
        KEYS = [c[1] for c in CAMPOS]
        self.tree_guia.bind("<<TreeviewSelect>>",
            lambda e: self._load_row(self.tree_guia,self.e_guia,KEYS))

    def _guia_insert(self):
        e=self.e_guia
        r=self.db.execute_procedure('sp_InsertGuia',
            e["Nombres"].get(),e["Apellidos"].get(),e["Documento"].get(),
            e["FechaNacimiento"].get() or None,e["Nacionalidad"].get(),
            e["Idiomas"].get(),e["Especialidades"].get(),e["Destinos"].get(),
            e["Certificaciones"].get(),e["Desempeño"].get() or None,
            e["Disponibilidad"].get())
        if r is not None:
            messagebox.showinfo("✔ Guardado","Guía guardado.")
            self._clear(self.e_guia); self._guia_all()

    def _guia_update(self):
        id_=self._req_id(self.e_guia,"IDGuia","IDGuia")
        if not id_: return
        e=self.e_guia
        r=self.db.execute_procedure('sp_UpdateGuia',id_,
            e["Nombres"].get(),e["Apellidos"].get(),e["Documento"].get(),
            e["FechaNacimiento"].get() or None,e["Nacionalidad"].get(),
            e["Idiomas"].get(),e["Especialidades"].get(),e["Destinos"].get(),
            e["Certificaciones"].get(),e["Desempeño"].get() or None,
            e["Disponibilidad"].get())
        if r is not None:
            messagebox.showinfo("✔ Actualizado","Guía actualizado.")
            self._guia_all()

    def _guia_delete(self):
        id_=self._req_id(self.e_guia,"IDGuia","IDGuia")
        if not id_: return
        if messagebox.askyesno("Confirmar","¿Eliminar este guía?"):
            r=self.db.execute_procedure('sp_DeleteGuia',id_)
            if r is not None:
                messagebox.showinfo("✔ Eliminado","Guía eliminado.")
                self._clear(self.e_guia); self._guia_all()

    def _guia_search(self):
        id_=self._req_id(self.e_guia,"IDGuia","IDGuia")
        if not id_: return
        r=self.db.execute_procedure('sp_GetGuia',id_)
        if r: self._populate(self.tree_guia,r)
        else: messagebox.showinfo("Sin resultados","Guía no encontrado.")

    def _guia_all(self):
        self._populate(self.tree_guia,self.db.execute_procedure('sp_GetAllGuias'))

    # ==========================================================
    # PESTAÑA 4 — CLIENTES
    # ==========================================================
    def _build_tab_clientes(self):
        self._banner(self.tab_cli,
                     "Gestión de Clientes",
                     TAB_BANNER_COLORS["cliente"], "cliente")
        form = self._scrollable_form(self.tab_cli)
        self.e_cli = {}
        CAMPOS = [
            ("ID Cliente:",               "IDCliente"),
            ("Tipo de cliente:",          "Tipo"),
            ("Nombres / Razón social:",   "NombreRazonSocial"),
            ("Documento:",                "Documento"),
            ("Nacionalidad:",             "Nacionalidad"),
            ("Dirección:",                "Direccion"),
            ("Teléfono:",                 "Telefono"),
            ("Correo electrónico:",       "Correo"),
            ("Preferencias de viaje:",    "Preferencias"),
            ("Historial de compras:",     "Historial"),
            ("Programa de fidelización:", "Fidelizacion"),
        ]
        for i,(lbl,key) in enumerate(CAMPOS): self._field(form,i,lbl,key,self.e_cli)
        self._buttons(self.tab_cli,{
            "Guardar":    self._cli_insert,
            "Actualizar": self._cli_update,
            "Eliminar":   self._cli_delete,
            "Limpiar":    lambda: self._clear(self.e_cli),
            "Buscar":     self._cli_search,
            "Ver Todos":  self._cli_all,
        })
        self.tree_cli = self._make_tree(self.tab_cli)
        KEYS = [c[1] for c in CAMPOS]
        self.tree_cli.bind("<<TreeviewSelect>>",
            lambda e: self._load_row(self.tree_cli,self.e_cli,KEYS))

    def _cli_insert(self):
        e=self.e_cli
        r=self.db.execute_procedure('sp_InsertCliente',
            e["Tipo"].get(),e["NombreRazonSocial"].get(),
            e["Documento"].get(),e["Nacionalidad"].get(),
            e["Direccion"].get(),e["Telefono"].get(),
            e["Correo"].get(),e["Preferencias"].get(),
            e["Historial"].get(),e["Fidelizacion"].get())
        if r is not None:
            messagebox.showinfo("✔ Guardado","Cliente guardado.")
            self._clear(self.e_cli); self._cli_all()

    def _cli_update(self):
        id_=self._req_id(self.e_cli,"IDCliente","IDCliente")
        if not id_: return
        e=self.e_cli
        r=self.db.execute_procedure('sp_UpdateCliente',id_,
            e["Tipo"].get(),e["NombreRazonSocial"].get(),
            e["Documento"].get(),e["Nacionalidad"].get(),
            e["Direccion"].get(),e["Telefono"].get(),
            e["Correo"].get(),e["Preferencias"].get(),
            e["Historial"].get(),e["Fidelizacion"].get())
        if r is not None:
            messagebox.showinfo("✔ Actualizado","Cliente actualizado.")
            self._cli_all()

    def _cli_delete(self):
        id_=self._req_id(self.e_cli,"IDCliente","IDCliente")
        if not id_: return
        if messagebox.askyesno("Confirmar","¿Eliminar este cliente?"):
            r=self.db.execute_procedure('sp_DeleteCliente',id_)
            if r is not None:
                messagebox.showinfo("✔ Eliminado","Cliente eliminado.")
                self._clear(self.e_cli); self._cli_all()

    def _cli_search(self):
        id_=self._req_id(self.e_cli,"IDCliente","IDCliente")
        if not id_: return
        r=self.db.execute_procedure('sp_GetCliente',id_)
        if r: self._populate(self.tree_cli,r)
        else: messagebox.showinfo("Sin resultados","Cliente no encontrado.")

    def _cli_all(self):
        self._populate(self.tree_cli,self.db.execute_procedure('sp_GetAllClientes'))


# =============================================================
# PUNTO DE ENTRADA
# =============================================================
if __name__ == "__main__":
    HOST     = "localhost"
    USER     = "root"
    PASSWORD = ""
    DATABASE = "destinos_sonados"

    db = DatabaseConnector(HOST, USER, PASSWORD, DATABASE)
    db.connect()

    app = DestinosSonadosApp(db)
    app.mainloop()

    db.disconnect()
