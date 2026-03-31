"""
Tech FAQ Chatbot - An AI-powered chatbot for answering technical questions
Features:
- NLP-based similarity matching for intelligent question answering
- Multiple tech categories (Programming, Web Dev, Data Science, Cloud, General)
- Admin panel to manage FAQs
- Persistent storage of FAQs in JSON format
- User-friendly CLI interface
"""

import json
import os
from difflib import SequenceMatcher
from typing import List, Tuple, Dict
import re

class TechFAQChatbot:
    def __init__(self, faq_file='tech_faq_database.json'):
        """Initialize the chatbot with FAQ database."""
        self.faq_file = faq_file
        self.similarity_threshold = 0.4
        self.faqs = self.load_faqs()
        
    def load_faqs(self) -> Dict:
        """Load FAQs from JSON file or create default database."""
        if os.path.exists(self.faq_file):
            try:
                with open(self.faq_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                print("Error reading FAQ file. Creating new database...")
                return self._create_default_faqs()
        else:
            return self._create_default_faqs()
    
    def _create_default_faqs(self) -> Dict:
        """Create default FAQ database with multiple tech categories."""
        faqs = {
            "General Tech": [
                {
                    "question": "What is artificial intelligence?",
                    "answer": "AI is a branch of computer science that focuses on creating intelligent machines capable of performing tasks that typically require human intelligence, such as learning, reasoning, and problem-solving.",
                    "category": "General Tech"
                },
                {
                    "question": "What is machine learning?",
                    "answer": "Machine learning is a subset of AI where systems learn from data and improve their performance without being explicitly programmed. It uses algorithms to find patterns in data.",
                    "category": "General Tech"
                },
                {
                    "question": "What is the difference between AI and ML?",
                    "answer": "AI is the broader field of creating intelligent systems, while ML is a specific approach within AI that focuses on learning from data. All ML is AI, but not all AI is ML.",
                    "category": "General Tech"
                },
                {
                    "question": "What is cloud computing?",
                    "answer": "Cloud computing is the delivery of computing services (servers, storage, databases, software) over the internet. It allows on-demand access to shared resources.",
                    "category": "General Tech"
                }
            ],
            "Programming": [
                {
                    "question": "What is Python?",
                    "answer": "Python is a high-level, interpreted programming language known for its simplicity and readability. It's widely used in web development, data science, and automation.",
                    "category": "Programming"
                },
                {
                    "question": "What is object-oriented programming?",
                    "answer": "OOP is a programming paradigm based on objects and classes. It emphasizes modularity, reusability, and encapsulation of data and methods.",
                    "category": "Programming"
                },
                {
                    "question": "What is a class in programming?",
                    "answer": "A class is a blueprint for creating objects. It defines attributes (properties) and methods (functions) that objects of that class will have.",
                    "category": "Programming"
                },
                {
                    "question": "What is an API?",
                    "answer": "An API (Application Programming Interface) is a set of protocols and tools for building software applications. It defines how software components should communicate.",
                    "category": "Programming"
                }
            ],
            "Web Development": [
                {
                    "question": "What is HTML?",
                    "answer": "HTML (HyperText Markup Language) is a markup language used to create web pages. It provides the structure and content of web pages.",
                    "category": "Web Development"
                },
                {
                    "question": "What is the difference between frontend and backend?",
                    "answer": "Frontend is the user-facing part of a web application (HTML, CSS, JavaScript), while backend is the server-side logic that processes data and manages the database.",
                    "category": "Web Development"
                },
                {
                    "question": "What is CSS?",
                    "answer": "CSS (Cascading Style Sheets) is used to style and layout web pages. It controls colors, fonts, spacing, and positioning of HTML elements.",
                    "category": "Web Development"
                },
                {
                    "question": "What is JavaScript?",
                    "answer": "JavaScript is a programming language that runs in web browsers. It enables interactive features and dynamic content on web pages.",
                    "category": "Web Development"
                }
            ],
            "Data Science": [
                {
                    "question": "What is data science?",
                    "answer": "Data science is an interdisciplinary field that combines statistics, programming, and domain knowledge to extract insights from data.",
                    "category": "Data Science"
                },
                {
                    "question": "What is a dataset?",
                    "answer": "A dataset is a collection of data points or records. It can be in various formats like CSV, JSON, or databases, and is used for analysis and training models.",
                    "category": "Data Science"
                },
                {
                    "question": "What is data preprocessing?",
                    "answer": "Data preprocessing involves cleaning and transforming raw data into a format suitable for analysis. It includes handling missing values, removing duplicates, and normalization.",
                    "category": "Data Science"
                },
                {
                    "question": "What is overfitting?",
                    "answer": "Overfitting occurs when a model learns the training data too well, including its noise. This causes poor generalization to new, unseen data.",
                    "category": "Data Science"
                }
            ],
            "Cloud & DevOps": [
                {
                    "question": "What is DevOps?",
                    "answer": "DevOps is a set of practices combining software development and IT operations. It aims for faster deployment, reliability, and better collaboration.",
                    "category": "Cloud & DevOps"
                },
                {
                    "question": "What is Docker?",
                    "answer": "Docker is a containerization platform that packages applications with their dependencies into containers. These containers can run consistently across different environments.",
                    "category": "Cloud & DevOps"
                },
                {
                    "question": "What is continuous integration?",
                    "answer": "Continuous Integration (CI) is a development practice where code changes are automatically tested and integrated into a shared repository multiple times a day.",
                    "category": "Cloud & DevOps"
                },
                {
                    "question": "What is AWS?",
                    "answer": "AWS (Amazon Web Services) is a cloud platform offering various services like computing, storage, databases, and networking on a pay-as-you-go basis.",
                    "category": "Cloud & DevOps"
                }
            ]
        }
        self.save_faqs(faqs)
        return faqs
    
    def save_faqs(self, faqs: Dict = None):
        """Save FAQs to JSON file."""
        data = faqs if faqs is not None else self.faqs
        with open(self.faq_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def calculate_similarity(self, text1: str, text2: str) -> float:
        """Calculate similarity score between two strings."""
        text1 = text1.lower().strip()
        text2 = text2.lower().strip()
        return SequenceMatcher(None, text1, text2).ratio()
    
    def preprocess_question(self, question: str) -> str:
        """Clean and normalize user question."""
        # Remove extra spaces and convert to lowercase
        question = ' '.join(question.split()).lower()
        # Remove common question words
        question = re.sub(r'^(what|how|why|is|can|do|tell|explain|describe)\s+', '', question)
        return question
    
    def find_best_match(self, user_question: str) -> Tuple[Dict, float]:
        """Find the best matching FAQ using NLP-based similarity."""
        preprocessed_user_question = self.preprocess_question(user_question)
        best_match = None
        best_score = 0
        
        for category, questions_list in self.faqs.items():
            for faq in questions_list:
                faq_question = faq['question']
                preprocessed_faq = self.preprocess_question(faq_question)
                
                # Calculate similarity score
                score = self.calculate_similarity(preprocessed_user_question, preprocessed_faq)
                
                if score > best_score:
                    best_score = score
                    best_match = faq
        
        return best_match, best_score
    
    def answer_question(self, user_question: str) -> str:
        """Find and return answer to user question."""
        best_match, confidence = self.find_best_match(user_question)
        
        if confidence >= self.similarity_threshold and best_match:
            response = f"\n📚 Found a match! (Confidence: {confidence*100:.1f}%)\n"
            response += f"Q: {best_match['question']}\n"
            response += f"A: {best_match['answer']}\n"
            response += f"📁 Category: {best_match['category']}\n"
            return response
        else:
            return "\n❌ Sorry, I couldn't find a relevant FAQ for your question.\n" + \
                   "Try asking with different keywords or use the admin panel to add this question.\n"
    
    def add_faq(self, question: str, answer: str, category: str) -> bool:
        """Add a new FAQ entry."""
        if category not in self.faqs:
            self.faqs[category] = []
        
        new_faq = {
            "question": question,
            "answer": answer,
            "category": category
        }
        self.faqs[category].append(new_faq)
        self.save_faqs()
        return True
    
    def delete_faq(self, question: str) -> bool:
        """Delete an FAQ entry."""
        for category in self.faqs.values():
            for i, faq in enumerate(category):
                if faq['question'].lower() == question.lower():
                    category.pop(i)
                    self.save_faqs()
                    return True
        return False
    
    def list_faqs_by_category(self, category: str = None) -> str:
        """List all FAQs or FAQs in a specific category."""
        if category:
            if category in self.faqs:
                faqs_list = self.faqs[category]
                response = f"\n📁 {category} FAQs:\n"
                response += "=" * 50 + "\n"
                for i, faq in enumerate(faqs_list, 1):
                    response += f"{i}. Q: {faq['question']}\n"
                    response += f"   A: {faq['answer'][:80]}...\n\n"
                return response
            else:
                return f"❌ Category '{category}' not found.\n"
        else:
            response = "\n📚 Available FAQ Categories:\n"
            response += "=" * 50 + "\n"
            for cat in self.faqs.keys():
                count = len(self.faqs[cat])
                response += f"• {cat} ({count} FAQs)\n"
            return response
    
    def show_help(self) -> str:
        """Display help information."""
        help_text = """
╔════════════════════════════════════════════════════════════════════╗
║               🤖 TECH FAQ CHATBOT - HELP MENU 🤖                   ║
╚════════════════════════════════════════════════════════════════════╝

👤 USER MODE COMMANDS:
  • Type any tech question and I'll find matching FAQs
  • 'list' - View all FAQ categories
  • 'list [category]' - View FAQs in a specific category
  • 'categories' - Show all available categories
  • 'admin' - Switch to admin mode
  • 'help' - Display this help message
  • 'exit' - Leave the chatbot

🔧 ADMIN MODE COMMANDS:
  • 'add' - Add a new FAQ
  • 'delete' - Delete an existing FAQ
  • 'list' - List all FAQs
  • 'back' - Return to user mode
  • 'help' - Show admin help
  • 'exit' - Leave the chatbot

📚 AVAILABLE CATEGORIES:
  • General Tech
  • Programming
  • Web Development
  • Data Science
  • Cloud & DevOps

💡 TIPS:
  • Ask natural questions like "What is Python?" or "How does ML work?"
  • The chatbot uses smart matching to find the best answer
  • Add FAQs in admin mode for questions that don't match well
"""
        return help_text
    
    def admin_panel(self):
        """Admin mode for managing FAQs."""
        print("\n🔧 Entering Admin Mode...")
        print("Type 'help' for admin commands or 'back' to return to user mode\n")
        
        while True:
            try:
                admin_input = input("Admin> ").strip()
                
                if not admin_input:
                    continue
                elif admin_input.lower() == 'back':
                    print("✅ Returning to user mode...\n")
                    break
                elif admin_input.lower() == 'help':
                    print("""
🔧 ADMIN COMMANDS:
  • 'add' - Add a new FAQ
  • 'delete' - Delete a FAQ by question
  • 'list' - Show all FAQs
  • 'list [category]' - Show FAQs in a category
  • 'back' - Return to user mode""")
                elif admin_input.lower() == 'add':
                    print("\n➕ ADD NEW FAQ")
                    print("Available categories:", ", ".join(self.faqs.keys()))
                    category = input("Category: ").strip()
                    if not category:
                        print("❌ Category cannot be empty!")
                        continue
                    question = input("Question: ").strip()
                    if not question:
                        print("❌ Question cannot be empty!")
                        continue
                    answer = input("Answer: ").strip()
                    if not answer:
                        print("❌ Answer cannot be empty!")
                        continue
                    
                    if self.add_faq(question, answer, category):
                        print("✅ FAQ added successfully!")
                    else:
                        print("❌ Failed to add FAQ!")
                
                elif admin_input.lower() == 'delete':
                    question = input("Enter question to delete: ").strip()
                    if self.delete_faq(question):
                        print("✅ FAQ deleted successfully!")
                    else:
                        print("❌ FAQ not found!")
                
                elif admin_input.lower().startswith('list'):
                    parts = admin_input.split(maxsplit=1)
                    if len(parts) > 1:
                        print(self.list_faqs_by_category(parts[1]))
                    else:
                        print(self.list_faqs_by_category())
                
                else:
                    print("❌ Unknown command. Type 'help' for available commands.")
            
            except KeyboardInterrupt:
                print("\n⚠️ Interrupted by user. Exiting admin mode...")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
    
    def run(self):
        """Main chatbot interaction loop."""
        print("\n" + "="*60)
        print("🤖 WELCOME TO TECH FAQ CHATBOT 🤖".center(60))
        print("="*60)
        print("\nYour AI-powered assistant for technical questions!")
        print("Type 'help' for commands or just ask a question.\n")
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                elif user_input.lower() == 'exit':
                    print("\n👋 Thanks for using Tech FAQ Chatbot! Goodbye!\n")
                    break
                
                elif user_input.lower() == 'help':
                    print(self.show_help())
                
                elif user_input.lower() == 'categories':
                    print(self.list_faqs_by_category())
                
                elif user_input.lower().startswith('list'):
                    parts = user_input.split(maxsplit=1)
                    if len(parts) > 1:
                        print(self.list_faqs_by_category(parts[1]))
                    else:
                        print(self.list_faqs_by_category())
                
                elif user_input.lower() == 'admin':
                    self.admin_panel()
                
                else:
                    print(self.answer_question(user_input))
            
            except KeyboardInterrupt:
                print("\n\n⚠️ Chat interrupted. Exiting...\n")
                break
            except Exception as e:
                print(f"❌ An error occurred: {e}\n")


def main():
    """Main entry point."""
    chatbot = TechFAQChatbot()
    chatbot.run()


if __name__ == "__main__":
    main()
