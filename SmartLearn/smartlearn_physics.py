import customtkinter as ctk
import random
import math
from typing import List, Dict, Tuple

# ======================
# COLOR SCHEME
# ======================
COLORS = {
    'bg': '#F8FAFC',
    'bg_secondary': '#EFF6FF',
    'primary': '#6366F1',
    'primary_light': '#818CF8',
    'primary_dark': '#4F46E5',
    'secondary': '#A78BFA',
    'success': '#10B981',
    'success_light': '#34D399',
    'warning': '#F59E0B',
    'error': '#EF4444',
    'card_bg': '#FFFFFF',
    'card_shadow': '#00000008',
    'text_dark': '#1E293B',
    'text_medium': '#475569',
    'text_light': '#64748B',
    'input_bg': '#F1F5F9',
    'input_border': '#E2E8F0',
    'hint_bg': '#DBEAFE',
    'hint_text': '#1E40AF',
    'kinematics': '#60A5FA',
    'freefall': '#A78BFA',
    'dynamics': '#F472B6',
    'work_energy': '#FBBF24',
    'momentum': '#34D399',
    'electricity': '#F87171',
    'vectors': '#818CF8'
}

# ======================
# REUSABLE UI COMPONENTS
# ======================
class RoundedButton(ctk.CTkButton):
    def __init__(self, master, text, command=None, color=None, **kwargs):
        super().__init__(
            master,
            text=text,
            command=command,
            corner_radius=25,
            height=55,
            font=("Poppins", 16, "bold"),
            fg_color=color or COLORS['primary'],
            hover_color=COLORS['primary_dark'] if color == COLORS['primary'] else color,
            border_width=0,
            text_color="#FFFFFF",
            **kwargs
        )

class ModernTopicCard(ctk.CTkButton):
    def __init__(self, master, topic_name, color, command=None, **kwargs):
        super().__init__(
            master,
            text=topic_name,
            command=command,
            corner_radius=20,
            height=90,
            width=160,
            font=("Poppins", 16, "bold"),
            fg_color=color,
            hover_color=color,
            text_color="#FFFFFF",
            border_width=0,
            **kwargs
        )

class TopicCard(ctk.CTkButton):
    def __init__(self, master, topic_name, color, command=None, **kwargs):
        super().__init__(
            master,
            text=topic_name,
            command=command,
            corner_radius=25,
            height=100,
            width=200,
            font=("Poppins", 18, "bold"),
            fg_color=color,
            hover_color=color,
            text_color="#FFFFFF",
            border_width=0,
            **kwargs
        )

class HintBubble(ctk.CTkFrame):
    def __init__(self, master, hint_text, **kwargs):
        super().__init__(
            master,
            corner_radius=20,
            fg_color=COLORS['hint_bg'],
            border_width=2,
            border_color=COLORS['primary_light'],
            **kwargs
        )
        
        self.label = ctk.CTkLabel(
            self,
            text=hint_text,
            font=("Poppins", 14),
            text_color=COLORS['hint_text'],
            wraplength=500,
            justify="left"
        )
        self.label.pack(padx=20, pady=15)

class StatsCard(ctk.CTkFrame):
    def __init__(self, master, icon, label, value, color, **kwargs):
        super().__init__(
            master,
            fg_color=COLORS['card_bg'],
            corner_radius=20,
            border_width=2,
            border_color=color,
            **kwargs
        )
        
        # Icon and label
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(padx=20, pady=(15, 5), fill="x")
        
        ctk.CTkLabel(
            header,
            text=icon,
            font=("Poppins", 28)
        ).pack(side="left", padx=(0, 10))
        
        ctk.CTkLabel(
            header,
            text=label,
            font=("Poppins", 14),
            text_color=COLORS['text_light']
        ).pack(side="left")
        
        # Value
        ctk.CTkLabel(
            self,
            text=value,
            font=("Poppins", 24, "bold"),
            text_color=color
        ).pack(padx=20, pady=(0, 15))

class ProgressBar(ctk.CTkFrame):
    def __init__(self, master, total, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        self.total = total
        self.current = 0
        
        self.bar_bg = ctk.CTkFrame(self, height=10, corner_radius=5, fg_color=COLORS['input_bg'])
        self.bar_bg.pack(fill="x", padx=20)
        
        self.bar_fill = ctk.CTkFrame(self.bar_bg, height=10, corner_radius=5, fg_color=COLORS['success'], width=0)
        self.bar_fill.place(x=0, y=0)
        
        self.label = ctk.CTkLabel(self, text="0 / 0", font=("Poppins", 12), text_color=COLORS['text_light'])
        self.label.pack(pady=5)

# ======================
# PROBLEM GENERATOR
# ======================
class PhysicsProblem:
    def __init__(self, topic: str, difficulty: str = "medium"):
        self.topic = topic
        self.difficulty = difficulty
        self.problem_text = ""
        self.answer = 0
        self.unit = ""
        self.hints = []
        self.solution = ""
        self.generate()
    
    def generate(self):
        if self.topic == "Kinematics":
            self.generate_kinematics()
        elif self.topic == "Free Fall":
            self.generate_freefall()
        elif self.topic == "Dynamics":
            self.generate_dynamics()
        elif self.topic == "Work & Energy":
            self.generate_work_energy()
        elif self.topic == "Momentum":
            self.generate_momentum()
        elif self.topic == "Electricity":
            self.generate_electricity()
        elif self.topic == "Vectors":
            self.generate_vectors()
        elif self.topic == "Projectile Motion":
            self.generate_projectile_motion()
        elif self.topic == "Unit Conversion":
            self.generate_unit_conversion()
    
    def generate_kinematics(self):
        problem_type = random.choice([1, 2, 3])
        
        if problem_type == 1:
            # Final velocity problem
            v0 = random.randint(5, 30)
            a = random.randint(2, 8)
            t = random.randint(3, 10)
            v = v0 + a * t
            
            self.problem_text = f"A car accelerates from {v0} m/s at {a} m/s² for {t} seconds.\nWhat is its final velocity?"
            self.answer = v
            self.unit = "m/s"
            
            self.hints = [
                "💡 Think about constant acceleration motion.",
                f"📐 Use the formula: v = v₀ + at",
                f"🔧 Initial velocity v₀ = {v0} m/s, acceleration a = {a} m/s², time t = {t} s",
                f"🧮 Calculate: v = {v0} + ({a} × {t}) = {v} m/s"
            ]
            
            self.solution = f"Using v = v₀ + at\nv = {v0} + ({a})({t})\nv = {v0} + {a*t}\nv = {v} m/s"
        
        elif problem_type == 2:
            # Distance problem
            v0 = random.randint(5, 20)
            a = random.randint(2, 8)
            t = random.randint(3, 8)
            s = v0 * t + 0.5 * a * t**2
            
            self.problem_text = f"A vehicle starts at {v0} m/s and accelerates at {a} m/s² for {t} seconds.\nHow far does it travel?"
            self.answer = round(s, 2)
            self.unit = "m"
            
            self.hints = [
                "💡 Use the kinematic equation for distance.",
                f"📐 Use: s = v₀t + ½at²",
                f"🔧 v₀ = {v0} m/s, a = {a} m/s², t = {t} s",
                f"🧮 s = {v0}({t}) + ½({a})({t}²) = {round(s, 2)} m"
            ]
            
            self.solution = f"s = v₀t + ½at²\ns = {v0}({t}) + ½({a})({t}²)\ns = {v0*t} + {0.5*a*t**2}\ns = {round(s, 2)} m"
        
        else:
            # Time problem
            v0 = random.randint(5, 20)
            v = random.randint(25, 50)
            a = random.randint(2, 8)
            t = (v - v0) / a
            
            self.problem_text = f"A car accelerates from {v0} m/s to {v} m/s at {a} m/s².\nHow long does this take?"
            self.answer = round(t, 2)
            self.unit = "s"
            
            self.hints = [
                "💡 Use the velocity equation to find time.",
                f"📐 Rearrange: v = v₀ + at → t = (v - v₀) / a",
                f"🔧 v = {v} m/s, v₀ = {v0} m/s, a = {a} m/s²",
                f"🧮 t = ({v} - {v0}) / {a} = {round(t, 2)} s"
            ]
            
            self.solution = f"v = v₀ + at\nt = (v - v₀) / a\nt = ({v} - {v0}) / {a}\nt = {round(t, 2)} s"
    
    def generate_freefall(self):
        problem_type = random.choice([1, 2])
        
        if problem_type == 1:
            # Time to fall problem
            h = random.randint(20, 100)
            g = 10
            t = math.sqrt(2 * h / g)
            
            self.problem_text = f"An object is dropped from a height of {h} meters.\nHow long does it take to reach the ground? (Use g = 10 m/s²)"
            self.answer = round(t, 2)
            self.unit = "s"
            
            self.hints = [
                "💡 This is free fall motion with initial velocity = 0.",
                f"📐 Use: h = ½gt²",
                f"🔧 Rearrange to solve for t: t = √(2h/g)",
                f"🧮 t = √(2×{h}/10) = √{2*h/10} ≈ {round(t, 2)} s"
            ]
            
            self.solution = f"h = ½gt²\n{h} = ½(10)t²\n{h} = 5t²\nt² = {h/5}\nt = √{h/5} ≈ {round(t, 2)} s"
        
        else:
            # Final velocity problem
            h = random.randint(20, 100)
            g = 10
            v = math.sqrt(2 * g * h)
            
            self.problem_text = f"An object falls freely from a height of {h} meters.\nWhat is its velocity just before hitting the ground? (Use g = 10 m/s²)"
            self.answer = round(v, 2)
            self.unit = "m/s"
            
            self.hints = [
                "💡 Use the kinematic equation for final velocity in free fall.",
                f"📐 Use: v² = 2gh (since v₀ = 0)",
                f"🔧 h = {h} m, g = 10 m/s²",
                f"🧮 v = √(2 × 10 × {h}) ≈ {round(v, 2)} m/s"
            ]
            
            self.solution = f"v² = 2gh\nv² = 2 × 10 × {h}\nv² = {2*g*h}\nv = √{2*g*h} ≈ {round(v, 2)} m/s"
    
    def generate_dynamics(self):
        problem_type = random.choice([1, 2, 3])
        
        if problem_type == 1:
            # Force problem
            m = random.randint(5, 50)
            a = random.randint(2, 10)
            F = m * a
            
            self.problem_text = f"A {m} kg object accelerates at {a} m/s².\nWhat is the net force acting on it?"
            self.answer = F
            self.unit = "N"
            
            self.hints = [
                "💡 Newton's Second Law connects force, mass, and acceleration.",
                "📐 Use F = ma",
                f"🔧 Mass = {m} kg, acceleration = {a} m/s²",
                f"🧮 F = {m} × {a} = {F} N"
            ]
            
            self.solution = f"Using F = ma\nF = {m} × {a}\nF = {F} N"
        
        elif problem_type == 2:
            # Mass problem
            F = random.randint(20, 200)
            a = random.randint(2, 10)
            m = F / a
            
            self.problem_text = f"A net force of {F} N acts on an object causing {a} m/s² acceleration.\nWhat is the mass of the object?"
            self.answer = round(m, 2)
            self.unit = "kg"
            
            self.hints = [
                "💡 Rearrange Newton's Second Law to find mass.",
                "📐 From F = ma, we get m = F/a",
                f"🔧 Force = {F} N, acceleration = {a} m/s²",
                f"🧮 m = {F} / {a} = {round(m, 2)} kg"
            ]
            
            self.solution = f"F = ma\nm = F/a\nm = {F} / {a}\nm = {round(m, 2)} kg"
        
        else:
            # Acceleration problem
            F = random.randint(20, 200)
            m = random.randint(5, 40)
            a = F / m
            
            self.problem_text = f"A {m} kg object experiences a net force of {F} N.\nWhat is its acceleration?"
            self.answer = round(a, 2)
            self.unit = "m/s²"
            
            self.hints = [
                "💡 Use Newton's Second Law to find acceleration.",
                "📐 From F = ma, we get a = F/m",
                f"🔧 Force = {F} N, Mass = {m} kg",
                f"🧮 a = {F} / {m} = {round(a, 2)} m/s²"
            ]
            
            self.solution = f"F = ma\na = F/m\na = {F} / {m}\na = {round(a, 2)} m/s²"
    
    def generate_work_energy(self):
        F = random.randint(10, 100)
        d = random.randint(5, 30)
        
        W = F * d
        
        self.problem_text = f"A force of {F} N moves an object {d} meters in the direction of the force.\nHow much work is done?"
        self.answer = W
        self.unit = "J"
        
        self.hints = [
            "💡 Work is force times displacement when they're parallel.",
            "📐 Use W = Fd (when force and displacement are parallel)",
            f"🔧 Force = {F} N, distance = {d} m",
            f"🧮 W = {F} × {d} = {W} J"
        ]
        
        self.solution = f"W = Fd\nW = {F} × {d}\nW = {W} J"
    
    def generate_momentum(self):
        m = random.randint(2, 20)
        v = random.randint(5, 30)
        
        p = m * v
        
        self.problem_text = f"A {m} kg object moves at {v} m/s.\nWhat is its momentum?"
        self.answer = p
        self.unit = "kg·m/s"
        
        self.hints = [
            "💡 Momentum is the product of mass and velocity.",
            "📐 Use p = mv",
            f"🔧 Mass = {m} kg, velocity = {v} m/s",
            f"🧮 p = {m} × {v} = {p} kg·m/s"
        ]
        
        self.solution = f"p = mv\np = {m} × {v}\np = {p} kg·m/s"
    
    def generate_electricity(self):
        V = random.randint(6, 24)
        R = random.randint(2, 12)
        
        I = V / R
        
        self.problem_text = f"A circuit has a voltage of {V} V and resistance of {R} Ω.\nWhat is the current?"
        self.answer = round(I, 2)
        self.unit = "A"
        
        self.hints = [
            "💡 Ohm's Law relates voltage, current, and resistance.",
            "📐 Use V = IR, so I = V/R",
            f"🔧 Voltage = {V} V, resistance = {R} Ω",
            f"🧮 I = {V}/{R} = {round(I, 2)} A"
        ]
        
        self.solution = f"I = V/R\nI = {V}/{R}\nI = {round(I, 2)} A"
    
    def generate_vectors(self):
        x = random.randint(3, 10)
        y = random.randint(3, 10)
        
        mag = math.sqrt(x**2 + y**2)
        
        self.problem_text = f"A vector has components: x = {x} m, y = {y} m.\nWhat is its magnitude?"
        self.answer = round(mag, 2)
        self.unit = "m"
        
        self.hints = [
            "💡 Use the Pythagorean theorem for vector magnitude.",
            "📐 |v| = √(x² + y²)",
            f"🔧 x = {x}, y = {y}",
            f"🧮 |v| = √({x}² + {y}²) = √{x**2 + y**2} ≈ {round(mag, 2)} m"
        ]
        
        self.solution = f"|v| = √(x² + y²)\n|v| = √({x}² + {y}²)\n|v| = √{x**2 + y**2}\n|v| ≈ {round(mag, 2)} m"
    
    def generate_projectile_motion(self):
        v0 = random.randint(10, 30)
        angle_deg = random.choice([30, 45, 60])
        angle_rad = math.radians(angle_deg)
        
        max_height = (v0**2 * math.sin(angle_rad)**2) / (2 * 10)
        
        self.problem_text = f"A projectile is launched at {v0} m/s at an angle of {angle_deg}° from the ground.\nWhat is the maximum height reached? (Use g = 10 m/s²)"
        self.answer = round(max_height, 2)
        self.unit = "m"
        
        self.hints = [
            "💡 This is projectile motion - we need the vertical component.",
            f"📐 Use: h_max = (v₀² sin²θ) / (2g)",
            f"🔧 Initial velocity = {v0} m/s, angle = {angle_deg}°, g = 10 m/s²",
            f"🧮 h_max = ({v0}² × sin²({angle_deg}°)) / 20 ≈ {round(max_height, 2)} m"
        ]
        
        self.solution = f"h_max = (v₀² sin²θ) / (2g)\nh_max = ({v0}² × sin²({angle_deg}°)) / (2 × 10)\nh_max = ({v0**2} × {round(math.sin(angle_rad)**2, 3)}) / 20\nh_max ≈ {round(max_height, 2)} m"
    
    def generate_unit_conversion(self):
        conversions = [
            ("kilometers", "meters", random.randint(1, 10), 1000, "km", "m"),
            ("grams", "kilograms", random.randint(100, 9000), 0.001, "g", "kg"),
            ("hours", "seconds", random.randint(1, 24), 3600, "h", "s"),
            ("centimeters", "meters", random.randint(10, 500), 0.01, "cm", "m"),
            ("milliliters", "liters", random.randint(100, 5000), 0.001, "mL", "L")
        ]
        
        from_unit, to_unit, value, factor, short_from, short_to = random.choice(conversions)
        result = value * factor
        
        self.problem_text = f"Convert {value} {short_from} to {short_to}."
        self.answer = round(result, 4)
        self.unit = short_to
        
        self.hints = [
            f"💡 You need to convert {short_from} to {short_to}.",
            f"📐 Conversion factor: 1 {short_from} = {factor} {short_to}",
            f"🔧 Starting value = {value} {short_from}",
            f"🧮 {value} × {factor} = {round(result, 4)} {short_to}"
        ]
        
        self.solution = f"{value} {short_from} × {factor}\n= {round(result, 4)} {short_to}"

# ======================
# MAIN APPLICATION
# ======================
class SmartLearnPhysics(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Window setup
        self.title("SmartLearn Physics - Master Physics with Intelligent Practice")
        self.geometry("1000x750")
        self.minsize(800, 600)
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        
        # App state
        self.current_problem = None
        self.hints_shown = 0
        self.score = 0
        self.problems_solved = 0
        self.mode = "Study"  # Study, Quiz, Exam
        
        # Container for all frames
        self.container = ctk.CTkFrame(self, fg_color=COLORS['bg'])
        self.container.pack(fill="both", expand=True)
        
        # Create all frames
        self.frames = {}
        for F in (HomeFrame, TopicFrame, ProblemFrame, ResultFrame):
            frame = F(self.container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        # Show home frame
        self.show_frame("HomeFrame")
    
    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()

# ======================
# HOME FRAME
# ======================
class HomeFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color=COLORS['bg'])
        self.controller = controller
        
        # Main container with better padding
        main_content = ctk.CTkScrollableFrame(self, fg_color=COLORS['bg'])
        main_content.pack(fill="both", expand=True, padx=0, pady=0)
        
        # Decorative header
        header_frame = ctk.CTkFrame(main_content, fg_color=COLORS['primary'], corner_radius=0)
        header_frame.pack(fill="x", pady=(0, 25))
        
        # Title
        title = ctk.CTkLabel(
            header_frame,
            text="🧪 SmartLearn Physics",
            font=("Poppins", 44, "bold"),
            text_color="#FFFFFF"
        )
        title.pack(pady=(35, 12))
        
        subtitle = ctk.CTkLabel(
            header_frame,
            text="Master Physics with Intelligent Practice",
            font=("Poppins", 16),
            text_color="#E0E0E0"
        )
        subtitle.pack(pady=(0, 35))
        
        # Stats cards display - constrained width
        stats_frame = ctk.CTkFrame(main_content, fg_color="transparent")
        stats_frame.pack(pady=20, padx=40, fill="x", expand=False)
        
        # Create two stat cards
        stat1_frame = ctk.CTkFrame(stats_frame, fg_color=COLORS['card_bg'], corner_radius=15, height=120)
        stat1_frame.pack(side="left", padx=5, fill="both", expand=True)
        stat1_frame.pack_propagate(False)
        
        ctk.CTkLabel(
            stat1_frame,
            text="🎯",
            font=("Poppins", 28)
        ).pack(pady=(8, 0))
        
        ctk.CTkLabel(
            stat1_frame,
            text="Problems",
            font=("Poppins", 12),
            text_color=COLORS['text_light']
        ).pack()
        
        self.problems_label = ctk.CTkLabel(
            stat1_frame,
            text=f"{controller.problems_solved}",
            font=("Poppins", 28, "bold"),
            text_color=COLORS['primary']
        )
        self.problems_label.pack(pady=(2, 8))
        
        stat2_frame = ctk.CTkFrame(stats_frame, fg_color=COLORS['card_bg'], corner_radius=15, height=120)
        stat2_frame.pack(side="left", padx=5, fill="both", expand=True)
        stat2_frame.pack_propagate(False)
        
        ctk.CTkLabel(
            stat2_frame,
            text="⭐",
            font=("Poppins", 28)
        ).pack(pady=(8, 0))
        
        ctk.CTkLabel(
            stat2_frame,
            text="Total XP",
            font=("Poppins", 12),
            text_color=COLORS['text_light']
        ).pack()
        
        self.xp_label = ctk.CTkLabel(
            stat2_frame,
            text=f"{controller.score}",
            font=("Poppins", 28, "bold"),
            text_color=COLORS['success']
        )
        self.xp_label.pack(pady=(2, 8))
        
        # Main action buttons
        btn_frame = ctk.CTkFrame(main_content, fg_color="transparent")
        btn_frame.pack(pady=15, padx=40, expand=False)
        
        RoundedButton(
            btn_frame,
            text="🚀 Start Practice",
            command=lambda: controller.show_frame("TopicFrame"),
            width=300
        ).pack(pady=8, anchor="center")
        
        # Secondary buttons (vertical)
        RoundedButton(
            btn_frame,
            text="📊 Progress",
            command=self.show_progress,
            color=COLORS['success'],
            width=300
        ).pack(pady=8, anchor="center")
        
        RoundedButton(
            btn_frame,
            text="ℹ️ Info",
            command=self.show_info,
            color=COLORS['primary_light'],
            width=300
        ).pack(pady=8, anchor="center")
        
        # Exit button
        RoundedButton(
            btn_frame,
            text="❌ Exit",
            command=controller.quit,
            color=COLORS['error'],
            width=300
        ).pack(pady=8, anchor="center")
    
    def show_info(self):
        popup = ctk.CTkToplevel(self)
        popup.title("About SmartLearn")
        popup.geometry("500x400")
        popup.resizable(False, False)
        
        # Center the popup
        popup.update_idletasks()
        x = self.winfo_x() + (self.winfo_width() - popup.winfo_width()) // 2
        y = self.winfo_y() + (self.winfo_height() - popup.winfo_height()) // 2
        popup.geometry(f"+{x}+{y}")
        
        header = ctk.CTkFrame(popup, fg_color=COLORS['primary'], corner_radius=0)
        header.pack(fill="x")
        
        ctk.CTkLabel(
            header,
            text="📚 About SmartLearn",
            font=("Poppins", 24, "bold"),
            text_color="#FFFFFF"
        ).pack(pady=20)
        
        # Info content frame
        info_frame = ctk.CTkFrame(popup, fg_color="transparent")
        info_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        info_text = ctk.CTkLabel(
            info_frame,
            text="Welcome to SmartLearn Physics!\n\n"
                 "An interactive learning platform that helps you master physics through:\n\n"
                 "✨ Interactive Problem Solving\n"
                 "💡 Intelligent Hints\n"
                 "📈 Progress Tracking\n"
                 "🎯 XP Reward System\n"
                 "🧠 Multiple Physics Topics\n\n"
                 "Practice problems across 9 different topics and track your progress!",
            font=("Poppins", 14),
            text_color=COLORS['text_dark'],
            wraplength=420,
            justify="left"
        )
        info_text.pack(pady=10, padx=10, anchor="nw", fill="both", expand=True)
        
        button_frame = ctk.CTkFrame(popup, fg_color="transparent")
        button_frame.pack(pady=15, padx=20, expand=False)
        
        RoundedButton(button_frame, text="Close", command=popup.destroy, width=150).pack(anchor="center")
    
    def show_progress(self):
        popup = ctk.CTkToplevel(self)
        popup.title("Your Progress")
        popup.geometry("500x450")
        popup.resizable(False, False)
        
        # Center the popup
        popup.update_idletasks()
        x = self.winfo_x() + (self.winfo_width() - popup.winfo_width()) // 2
        y = self.winfo_y() + (self.winfo_height() - popup.winfo_height()) // 2
        popup.geometry(f"+{x}+{y}")
        
        header = ctk.CTkFrame(popup, fg_color=COLORS['primary'], corner_radius=0)
        header.pack(fill="x")
        
        ctk.CTkLabel(
            header,
            text="📊 Your Progress",
            font=("Poppins", 24, "bold"),
            text_color="#FFFFFF"
        ).pack(pady=20)
        
        # Progress stats - scrollable
        stats_scroll = ctk.CTkScrollableFrame(popup, fg_color="transparent")
        stats_scroll.pack(fill="both", expand=True, padx=20, pady=20)
        
        stat_items = [
            ("🎯 Problems Solved", str(self.controller.problems_solved), COLORS['primary']),
            ("⭐ Total XP Earned", str(self.controller.score), COLORS['success']),
            ("📈 Average per Problem", str(self.controller.score // max(1, self.controller.problems_solved)) if self.controller.problems_solved > 0 else "0", COLORS['warning'])
        ]
        
        for icon_label, value, color in stat_items:
            stat_frame = ctk.CTkFrame(stats_scroll, fg_color=COLORS['card_bg'], corner_radius=15)
            stat_frame.pack(fill="x", pady=8)
            
            left = ctk.CTkLabel(stat_frame, text=icon_label, font=("Poppins", 14), text_color=COLORS['text_dark'])
            left.pack(side="left", padx=20, pady=15)
            
            right = ctk.CTkLabel(stat_frame, text=value, font=("Poppins", 18, "bold"), text_color=color)
            right.pack(side="right", padx=20, pady=15)
        
        # Motivational message
        msg_frame = ctk.CTkFrame(stats_scroll, fg_color=COLORS['hint_bg'], corner_radius=15, border_width=2, border_color=COLORS['primary_light'])
        msg_frame.pack(fill="x", pady=8, padx=0)
        
        motivation = "🌟 Keep it up! You're doing great! 🌟"
        if self.controller.problems_solved > 10:
            motivation = "🔥 Amazing progress! You're unstoppable! 🔥"
        elif self.controller.problems_solved > 5:
            motivation = "💪 Great work! Keep practicing! 💪"
        
        ctk.CTkLabel(
            msg_frame,
            text=motivation,
            font=("Poppins", 14, "bold"),
            text_color=COLORS['hint_text'],
            wraplength=380,
            justify="center"
        ).pack(padx=15, pady=15)
        
        # Close button at bottom
        button_frame = ctk.CTkFrame(popup, fg_color="transparent")
        button_frame.pack(pady=15, padx=20, expand=False)
        
        RoundedButton(button_frame, text="Close", command=popup.destroy, width=150).pack(anchor="center")
    
    def tkraise(self):
        super().tkraise()
        # Update stats
        self.problems_label.configure(text=str(self.controller.problems_solved))
        self.xp_label.configure(text=str(self.controller.score))

# ======================
# TOPIC SELECTION FRAME
# ======================
class TopicFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color=COLORS['bg'])
        self.controller = controller
        
        # Main scrollable container
        main_content = ctk.CTkScrollableFrame(self, fg_color=COLORS['bg'])
        main_content.pack(fill="both", expand=True, padx=0, pady=0)
        
        # Header with gradient effect
        header_frame = ctk.CTkFrame(main_content, fg_color=COLORS['primary'], corner_radius=0)
        header_frame.pack(fill="x", pady=(0, 40))
        
        title = ctk.CTkLabel(
            header_frame,
            text="📚 Choose Your Topic",
            font=("Poppins", 36, "bold"),
            text_color="#FFFFFF"
        )
        title.pack(pady=(30, 10))
        
        subtitle = ctk.CTkLabel(
            header_frame,
            text="Select a physics topic to start practicing",
            font=("Poppins", 13),
            text_color="#E0E0E0"
        )
        subtitle.pack(pady=(0, 25))
        
        # Topics grid with improved spacing
        topics_container = ctk.CTkFrame(main_content, fg_color="transparent")
        topics_container.pack(expand=False, padx=40, pady=20, fill="x")
        
        topics = [
            ("⚙️ Kinematics", COLORS['kinematics']),
            ("⬇️ Free Fall", COLORS['freefall']),
            ("🚗 Dynamics", COLORS['dynamics']),
            ("⚡ Work & Energy", COLORS['work_energy']),
            ("💫 Momentum", COLORS['momentum']),
            ("🔌 Electricity", COLORS['electricity']),
            ("➡️ Vectors", COLORS['vectors']),
            ("🎯 Projectile Motion", COLORS['warning']),
            ("📏 Unit Conversion", COLORS['secondary'])
        ]
        
        row, col = 0, 0
        for topic, color in topics:
            # Extract topic name (remove emoji)
            topic_name = topic.split(" ", 1)[1] if " " in topic else topic
            
            card = ModernTopicCard(
                topics_container,
                topic,
                color,
                command=lambda t=topic_name: self.select_topic(t)
            )
            card.grid(row=row, column=col, padx=10, pady=10, sticky="ew")
            
            col += 1
            if col > 2:
                col = 0
                row += 1
        
        # Configure grid weights for proper spacing
        topics_container.grid_columnconfigure(0, weight=1, minsize=180)
        topics_container.grid_columnconfigure(1, weight=1, minsize=180)
        topics_container.grid_columnconfigure(2, weight=1, minsize=180)
        
        # Back button at bottom
        footer_frame = ctk.CTkFrame(main_content, fg_color="transparent")
        footer_frame.pack(pady=15, padx=40, expand=False)
        
        RoundedButton(
            footer_frame,
            text="← Back to Home",
            command=lambda: controller.show_frame("HomeFrame"),
            color=COLORS['text_light'],
            width=300
        ).pack(anchor="center")
    
    def select_topic(self, topic):
        self.controller.current_problem = PhysicsProblem(topic)
        self.controller.hints_shown = 0
        problem_frame = self.controller.frames["ProblemFrame"]
        problem_frame.load_problem()
        self.controller.show_frame("ProblemFrame")

# ======================
# PROBLEM FRAME
# ======================
class ProblemFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color=COLORS['bg'])
        self.controller = controller
        
        # Header
        header = ctk.CTkFrame(self, fg_color=COLORS['primary_light'], corner_radius=0)
        header.pack(fill="x", padx=0, pady=0)
        
        ctk.CTkLabel(
            header,
            text="🎯 Problem Solving",
            font=("Poppins", 28, "bold"),
            text_color="#FFFFFF"
        ).pack(pady=20)
        
        # Scrollable frame for content
        self.main_container = ctk.CTkScrollableFrame(self, fg_color=COLORS['bg'])
        self.main_container.pack(fill="both", expand=True, padx=0, pady=0)
        
        content_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        content_frame.pack(fill="both", expand=True, padx=30, pady=30)
        
        # Problem card with modern design
        self.problem_card = ctk.CTkFrame(content_frame, fg_color=COLORS['card_bg'], corner_radius=25, border_width=2, border_color=COLORS['input_border'])
        self.problem_card.pack(pady=20, fill="x")
        
        self.problem_label = ctk.CTkLabel(
            self.problem_card,
            text="",
            font=("Poppins", 20),
            text_color=COLORS['text_dark'],
            wraplength=700,
            justify="center"
        )
        self.problem_label.pack(pady=40, padx=40)
        
        # Input section with better styling
        input_section = ctk.CTkFrame(content_frame, fg_color=COLORS['card_bg'], corner_radius=25, border_width=2, border_color=COLORS['input_border'])
        input_section.pack(pady=20, fill="x")
        
        ctk.CTkLabel(
            input_section,
            text="Your Answer",
            font=("Poppins", 16, "bold"),
            text_color=COLORS['text_dark']
        ).pack(pady=(20, 10), padx=40)
        
        self.answer_entry = ctk.CTkEntry(
            input_section,
            width=300,
            height=55,
            corner_radius=15,
            font=("Poppins", 18),
            fg_color=COLORS['input_bg'],
            border_color=COLORS['primary'],
            border_width=2,
            placeholder_text="Enter your answer..."
        )
        self.answer_entry.pack(pady=(0, 20), padx=40)
        
        # Buttons with improved layout
        btn_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
        btn_frame.pack(pady=20, expand=False)
        
        RoundedButton(
            btn_frame,
            text="✓ Check Answer",
            command=self.check_answer,
            width=220
        ).pack(pady=8, anchor="center")
        
        RoundedButton(
            btn_frame,
            text="💡 Show Hint",
            command=self.show_hint,
            color=COLORS['warning'],
            width=220
        ).pack(pady=8, anchor="center")
        
        RoundedButton(
            btn_frame,
            text="→ Skip",
            command=self.next_problem,
            color=COLORS['text_light'],
            width=220
        ).pack(pady=8, anchor="center")
        
        # Hints container
        self.hints_container = ctk.CTkFrame(content_frame, fg_color="transparent")
        self.hints_container.pack(pady=20, fill="x")
        
        # Back button
        footer = ctk.CTkFrame(content_frame, fg_color="transparent")
        footer.pack(pady=20, expand=False)
        
        RoundedButton(
            footer,
            text="← Back to Topics",
            command=lambda: controller.show_frame("TopicFrame"),
            color=COLORS['text_light'],
            width=300
        ).pack(anchor="center")
    
    def load_problem(self):
        problem = self.controller.current_problem
        self.problem_label.configure(text=problem.problem_text)
        self.answer_entry.delete(0, 'end')
        
        # Clear hints
        for widget in self.hints_container.winfo_children():
            widget.destroy()
        
        self.controller.hints_shown = 0
    
    def show_hint(self):
        problem = self.controller.current_problem
        hints_shown = self.controller.hints_shown
        
        if hints_shown < len(problem.hints):
            hint = problem.hints[hints_shown]
            bubble = HintBubble(self.hints_container, hint)
            bubble.pack(pady=10, anchor="w", fill="x", padx=10)
            self.controller.hints_shown += 1
            self.main_container._parent_canvas.yview_moveto(1)  # Scroll to bottom
        else:
            self.show_message("✨ You've seen all hints! Try solving now!")
    
    def check_answer(self):
        user_answer = self.answer_entry.get().strip()
        
        if not user_answer:
            self.show_message("⚠️ Please enter an answer!")
            return
        
        try:
            user_value = float(user_answer)
            correct_answer = self.controller.current_problem.answer
            
            # Check with tolerance
            tolerance = abs(correct_answer * 0.02)  # 2% tolerance
            
            if abs(user_value - correct_answer) <= tolerance:
                # Correct!
                xp_earned = 10 - (self.controller.hints_shown * 2)
                xp_earned = max(xp_earned, 2)
                self.controller.score += xp_earned
                self.controller.problems_solved += 1
                
                result_frame = self.controller.frames["ResultFrame"]
                result_frame.show_result(True, xp_earned)
                self.controller.show_frame("ResultFrame")
            else:
                # Wrong answer
                result_frame = self.controller.frames["ResultFrame"]
                result_frame.show_result(False, 0)
                self.controller.show_frame("ResultFrame")
        
        except ValueError:
            self.show_message("⚠️ Please enter a valid number!")
    
    def next_problem(self):
        self.controller.show_frame("TopicFrame")
    
    def show_message(self, msg):
        bubble = HintBubble(self.hints_container, msg)
        bubble.pack(pady=10, anchor="w", fill="x", padx=10)
        self.after(3000, bubble.destroy)

# ======================
# RESULT FRAME
# ======================
class ResultFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color=COLORS['bg'])
        self.controller = controller
        
        # Main container
        main_container = ctk.CTkScrollableFrame(self, fg_color=COLORS['bg'])
        main_container.pack(fill="both", expand=True, padx=0, pady=0)
        
        # Header
        header = ctk.CTkFrame(main_container, fg_color=COLORS['success'], corner_radius=0)
        header.pack(fill="x", padx=0, pady=(0, 40))
        
        self.emoji_label = ctk.CTkLabel(
            header,
            text="🎉",
            font=("Poppins", 60)
        )
        self.emoji_label.pack(pady=20)
        
        # Result card
        self.result_card = ctk.CTkFrame(main_container, fg_color=COLORS['card_bg'], corner_radius=30, border_width=2, border_color=COLORS['success'])
        self.result_card.pack(expand=True, padx=40, pady=20, fill="both")
        
        self.result_text = ctk.CTkLabel(
            self.result_card,
            text="Great Job!",
            font=("Poppins", 36, "bold"),
            text_color=COLORS['success']
        )
        self.result_text.pack(pady=(30, 10))
        
        self.detail_text = ctk.CTkLabel(
            self.result_card,
            text="",
            font=("Poppins", 16),
            text_color=COLORS['text_dark'],
            wraplength=600,
            justify="center"
        )
        self.detail_text.pack(pady=20, padx=40)
        
        self.solution_text = ctk.CTkLabel(
            self.result_card,
            text="",
            font=("Poppins", 13),
            text_color=COLORS['text_medium'],
            wraplength=600,
            justify="left"
        )
        self.solution_text.pack(pady=10, padx=40)
        
        # XP badge
        self.xp_badge = ctk.CTkFrame(self.result_card, fg_color=COLORS['primary_light'], corner_radius=15)
        self.xp_badge.pack(pady=20)
        
        self.xp_text = ctk.CTkLabel(
            self.xp_badge,
            text="+10 XP",
            font=("Poppins", 20, "bold"),
            text_color="#FFFFFF"
        )
        self.xp_text.pack(padx=30, pady=15)
        
        # Buttons
        btn_frame = ctk.CTkFrame(self.result_card, fg_color="transparent")
        btn_frame.pack(pady=30, padx=30, expand=False)
        
        RoundedButton(
            btn_frame,
            text="🔄 Try Again",
            command=self.try_again,
            width=220
        ).pack(pady=8, anchor="center")
        
        RoundedButton(
            btn_frame,
            text="→ Next Problem",
            command=self.next_problem,
            color=COLORS['success'],
            width=220
        ).pack(pady=8, anchor="center")
        
        RoundedButton(
            btn_frame,
            text="🏠 Home",
            command=lambda: controller.show_frame("HomeFrame"),
            color=COLORS['text_light'],
            width=220
        ).pack(pady=8, anchor="center")
    
    def show_result(self, correct, xp_earned):
        problem = self.controller.current_problem
        
        if correct:
            self.emoji_label.configure(text="🎉")
            self.result_text.configure(text="Excellent!", text_color=COLORS['success'])
            self.detail_text.configure(
                text=f"You got it right!\n\nCorrect answer: {problem.answer} {problem.unit}"
            )
            self.xp_text.configure(text=f"+{xp_earned} XP 🌟")
            self.xp_badge.configure(fg_color=COLORS['success'])
            self.solution_text.configure(text="")
        else:
            self.emoji_label.configure(text="🤔")
            self.result_text.configure(text="Not Quite Right", text_color=COLORS['warning'])
            self.detail_text.configure(
                text=f"The correct answer is: {problem.answer} {problem.unit}\n\nDon't worry! Keep practicing and you'll master this! 💪"
            )
            self.xp_text.configure(text="0 XP - Try Again")
            self.xp_badge.configure(fg_color=COLORS['warning'])
            self.solution_text.configure(text=f"📚 Solution:\n{problem.solution}")
    
    def try_again(self):
        problem_frame = self.controller.frames["ProblemFrame"]
        problem_frame.load_problem()
        self.controller.show_frame("ProblemFrame")
    
    def next_problem(self):
        self.controller.show_frame("TopicFrame")

# ======================
# RUN APPLICATION
# ======================
if __name__ == "__main__":
    app = SmartLearnPhysics()
    app.mainloop()
  
