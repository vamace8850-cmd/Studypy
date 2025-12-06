#!/usr/bin/env python3
"""
Force & Motion Quiz PowerPoint Generator
This script adds all 25 MCQs to a PowerPoint presentation with:
- Modern slide design
- Interactive buttons
- AI Assistant integration
- Smooth transitions
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.oxml.xmlchemy import OxmlElement
from datetime import datetime
import json
import os

# Color scheme matching neo-edu glow theme
COLOR_DARK_BG = RGBColor(15, 15, 26)      # #0f0f1a
COLOR_PRIMARY = RGBColor(252, 235, 210)   # #fcebd2 (warm white)
COLOR_ACCENT = RGBColor(211, 162, 111)    # #d3a26f (gold/copper)
COLOR_BLUE = RGBColor(68, 202, 255)       # #44caff (bright blue)
COLOR_CORRECT = RGBColor(58, 255, 98)     # #3aff62 (neon green)
COLOR_INCORRECT = RGBColor(255, 46, 87)   # #ff2e57 (neon red)
COLOR_TEXT = RGBColor(224, 224, 224)      # #e0e0e0 (light gray)
COLOR_SUBTLE = RGBColor(153, 153, 153)    # #999999 (subtle gray)


def load_quiz_data(json_path='data/quiz-mcq-force-motion.json'):
    """Load quiz questions from JSON"""
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['quizzes'][0]  # Get first quiz


def add_title_slide(prs):
    """Add title slide for quiz zone"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank layout
    
    # Set background
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = COLOR_DARK_BG
    
    # Add title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(2), Inches(9), Inches(1.5))
    title_frame = title_box.text_frame
    title_frame.word_wrap = True
    
    p = title_frame.paragraphs[0]
    p.text = "📚 Force & Motion Quiz Zone"
    p.font.size = Pt(66)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY
    p.alignment = PP_ALIGN.CENTER
    
    # Add subtitle
    subtitle_box = slide.shapes.add_textbox(Inches(0.5), Inches(3.7), Inches(9), Inches(0.8))
    subtitle_frame = subtitle_box.text_frame
    subtitle_frame.word_wrap = True
    
    p = subtitle_frame.paragraphs[0]
    p.text = "Test Your Knowledge on Balanced & Unbalanced Forces"
    p.font.size = Pt(24)
    p.font.color.rgb = COLOR_BLUE
    p.alignment = PP_ALIGN.CENTER
    
    # Add quiz stats
    stats_box = slide.shapes.add_textbox(Inches(2), Inches(5), Inches(7), Inches(1.5))
    stats_frame = stats_box.text_frame
    stats_frame.word_wrap = True
    
    stats_text = stats_frame.paragraphs[0]
    stats_text.text = "✅ 25 Questions  •  ⏱️ 90 Seconds Per Question  •  🎯 70% Passing Score"
    stats_text.font.size = Pt(20)
    stats_text.font.color.rgb = COLOR_ACCENT
    stats_text.alignment = PP_ALIGN.CENTER
    
    # Add start button placeholder
    button_box = slide.shapes.add_textbox(Inches(3.5), Inches(6.8), Inches(3), Inches(0.6))
    button_frame = button_box.text_frame
    button_frame.word_wrap = True
    
    p = button_frame.paragraphs[0]
    p.text = "▶ START QUIZ"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = COLOR_DARK_BG
    p.alignment = PP_ALIGN.CENTER
    
    # Add button background
    shape = slide.shapes.add_shape(
        1,  # Rectangle
        Inches(3.5), Inches(6.8), Inches(3), Inches(0.6)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = COLOR_ACCENT
    shape.line.color.rgb = COLOR_ACCENT
    shape.line.width = Pt(2)
    
    # Send to back
    slide.shapes._spTree.remove(shape._element)
    slide.shapes._spTree.insert(2, shape._element)


def add_question_slide(prs, question_data, question_num):
    """Add a question slide with options and AI button"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank layout
    
    # Set background
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = COLOR_DARK_BG
    
    # Question number and progress
    header_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.5))
    header_frame = header_box.text_frame
    p = header_frame.paragraphs[0]
    p.text = f"Question {question_num} of 25"
    p.font.size = Pt(14)
    p.font.color.rgb = COLOR_SUBTLE
    p.alignment = PP_ALIGN.LEFT
    
    # Question text
    q_box = slide.shapes.add_textbox(Inches(0.5), Inches(1), Inches(8.5), Inches(1.2))
    q_frame = q_box.text_frame
    q_frame.word_wrap = True
    
    p = q_frame.paragraphs[0]
    p.text = question_data['question']
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY
    p.line_spacing = 1.3
    
    # Add options
    start_y = 2.4
    for idx, option in enumerate(question_data['options']):
        option_box = slide.shapes.add_textbox(
            Inches(0.8), Inches(start_y + idx * 0.8), Inches(8), Inches(0.7)
        )
        option_frame = option_box.text_frame
        option_frame.word_wrap = True
        
        p = option_frame.paragraphs[0]
        letter = chr(65 + idx)  # A, B, C, D
        p.text = f"{letter}) {option}"
        p.font.size = Pt(16)
        p.font.color.rgb = COLOR_TEXT
        
        # Add background box for option
        option_shape = slide.shapes.add_shape(
            1,  # Rectangle
            Inches(0.7), Inches(start_y + idx * 0.8), Inches(8.3), Inches(0.7)
        )
        option_shape.fill.solid()
        option_shape.fill.fore_color.rgb = RGBColor(25, 25, 45)
        option_shape.fill.transparency = 0.5
        option_shape.line.color.rgb = COLOR_ACCENT
        option_shape.line.width = Pt(1)
        
        # Send to back
        slide.shapes._spTree.remove(option_shape._element)
        slide.shapes._spTree.insert(2, option_shape._element)
    
    # Add "Show Answer" button
    show_ans_box = slide.shapes.add_textbox(Inches(1), Inches(6.5), Inches(2.5), Inches(0.5))
    show_ans_frame = show_ans_box.text_frame
    p = show_ans_frame.paragraphs[0]
    p.text = "👁️ SHOW ANSWER"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY
    p.alignment = PP_ALIGN.CENTER
    
    show_ans_shape = slide.shapes.add_shape(
        1,  # Rectangle
        Inches(1), Inches(6.5), Inches(2.5), Inches(0.5)
    )
    show_ans_shape.fill.solid()
    show_ans_shape.fill.fore_color.rgb = RGBColor(40, 40, 60)
    show_ans_shape.line.color.rgb = COLOR_PRIMARY
    show_ans_shape.line.width = Pt(2)
    slide.shapes._spTree.remove(show_ans_shape._element)
    slide.shapes._spTree.insert(2, show_ans_shape._element)
    
    # Add "Ask AI" button
    ask_ai_box = slide.shapes.add_textbox(Inches(3.8), Inches(6.5), Inches(2.5), Inches(0.5))
    ask_ai_frame = ask_ai_box.text_frame
    p = ask_ai_frame.paragraphs[0]
    p.text = "🤖 ASK AI"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_DARK_BG
    p.alignment = PP_ALIGN.CENTER
    
    ask_ai_shape = slide.shapes.add_shape(
        1,  # Rectangle
        Inches(3.8), Inches(6.5), Inches(2.5), Inches(0.5)
    )
    ask_ai_shape.fill.solid()
    ask_ai_shape.fill.fore_color.rgb = COLOR_BLUE
    ask_ai_shape.line.color.rgb = COLOR_BLUE
    ask_ai_shape.line.width = Pt(2)
    slide.shapes._spTree.remove(ask_ai_shape._element)
    slide.shapes._spTree.insert(2, ask_ai_shape._element)
    
    # Add "Next Question" button
    next_box = slide.shapes.add_textbox(Inches(6.6), Inches(6.5), Inches(2.5), Inches(0.5))
    next_frame = next_box.text_frame
    p = next_frame.paragraphs[0]
    p.text = "NEXT ➡️"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_DARK_BG
    p.alignment = PP_ALIGN.CENTER
    
    next_shape = slide.shapes.add_shape(
        1,  # Rectangle
        Inches(6.6), Inches(6.5), Inches(2.5), Inches(0.5)
    )
    next_shape.fill.solid()
    next_shape.fill.fore_color.rgb = COLOR_ACCENT
    next_shape.line.color.rgb = COLOR_ACCENT
    next_shape.line.width = Pt(2)
    slide.shapes._spTree.remove(next_shape._element)
    slide.shapes._spTree.insert(2, next_shape._element)
    
    # Add answer explanation section (below fold)
    answer_section = slide.shapes.add_textbox(Inches(0.5), Inches(7.3), Inches(9), Inches(0.8))
    answer_frame = answer_section.text_frame
    answer_frame.word_wrap = True
    
    p = answer_frame.paragraphs[0]
    p.text = f"✅ Correct Answer: {chr(65 + question_data['correctAnswer'])})"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_CORRECT
    
    # Add explanation
    explanation_box = slide.shapes.add_textbox(Inches(0.5), Inches(8.15), Inches(9), Inches(0.8))
    explanation_frame = explanation_box.text_frame
    explanation_frame.word_wrap = True
    
    p = explanation_frame.paragraphs[0]
    p.text = f"💡 {question_data['explanation']}"
    p.font.size = Pt(11)
    p.font.color.rgb = COLOR_TEXT
    p.line_spacing = 1.2


def add_results_slide(prs):
    """Add final results/completion slide"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank layout
    
    # Set background
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = COLOR_DARK_BG
    
    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(2), Inches(9), Inches(1))
    title_frame = title_box.text_frame
    
    p = title_frame.paragraphs[0]
    p.text = "🎉 Quiz Completed!"
    p.font.size = Pt(54)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY
    p.alignment = PP_ALIGN.CENTER
    
    # Subtitle
    subtitle_box = slide.shapes.add_textbox(Inches(0.5), Inches(3.3), Inches(9), Inches(0.8))
    subtitle_frame = subtitle_box.text_frame
    
    p = subtitle_frame.paragraphs[0]
    p.text = "Check Your Score on StudyPy Website"
    p.font.size = Pt(20)
    p.font.color.rgb = COLOR_ACCENT
    p.alignment = PP_ALIGN.CENTER
    
    # Stats
    stats_box = slide.shapes.add_textbox(Inches(2), Inches(4.5), Inches(7), Inches(2))
    stats_frame = stats_box.text_frame
    stats_frame.word_wrap = True
    
    p = stats_frame.paragraphs[0]
    p.text = "✅ All 25 Questions Completed\n📊 Detailed Score Analysis\n🏆 Performance Report"
    p.font.size = Pt(18)
    p.font.color.rgb = COLOR_TEXT
    p.line_spacing = 1.5
    p.alignment = PP_ALIGN.CENTER
    
    # Link section
    link_box = slide.shapes.add_textbox(Inches(1.5), Inches(7), Inches(7), Inches(1))
    link_frame = link_box.text_frame
    link_frame.word_wrap = True
    
    p = link_frame.paragraphs[0]
    p.text = "Visit: http://localhost:8000/quiz-force-motion.html"
    p.font.size = Pt(16)
    p.font.color.rgb = COLOR_BLUE
    p.alignment = PP_ALIGN.CENTER


def create_quiz_presentation(output_path='StudyPy_Force_Motion_Quiz.pptx'):
    """Create complete quiz presentation"""
    
    # Load quiz data
    quiz_data = load_quiz_data()
    
    # Create presentation
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)
    
    print(f"Creating quiz presentation with {len(quiz_data['questions'])} questions...")
    
    # Add title slide
    add_title_slide(prs)
    print("✅ Added title slide")
    
    # Add question slides
    for idx, question in enumerate(quiz_data['questions'], 1):
        add_question_slide(prs, question, idx)
        print(f"✅ Added question {idx}/25")
    
    # Add results slide
    add_results_slide(prs)
    print("✅ Added results slide")
    
    # Save presentation
    prs.save(output_path)
    print(f"\n🎉 Presentation created: {output_path}")
    print(f"📏 Total slides: {len(prs.slides)}")
    
    return output_path


if __name__ == '__main__':
    try:
        create_quiz_presentation()
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        print("Make sure the quiz JSON file exists at: data/quiz-mcq-force-motion.json")
    except Exception as e:
        print(f"❌ Error creating presentation: {e}")
