from agents.user_profile_agent import UserProfileAgent
from agents.meal_planner_agent import DailyMealPlanner
from agents.feedback_agent import FeedbackAgent
from agents.llm_explanation_agent import LLMExplanationAgent
from llm.llama_loader import LlamaLoader


class NutritionOrchestrator:
    def __init__(self):
        self.llm_loader = LlamaLoader()
        self.explainer = LLMExplanationAgent(self.llm_loader.generate)

    def run_day(self, user_input, feedback=None):
        profile = UserProfileAgent(user_input).build_profile()

        if feedback:
            feedback_agent = FeedbackAgent(feedback["yesterday_plan"], feedback)
            adjustments = feedback_agent.generate_adjustments()
        else:
            adjustments = None

        planner = DailyMealPlanner(profile, adjustments)
        plan = planner.generate_day_plan()

        explanation = self.explainer.explain_day_plan(
            user_profile=profile,
            day_plan=plan,
            feedback_adjustments=feedback
        )

        return {
            "profile": profile,
            "plan": plan,
            "explanation": explanation
        }
