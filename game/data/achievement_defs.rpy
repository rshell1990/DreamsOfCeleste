default _enable_achievements = True

init python:
    achievement.steam_position = "bottom right"

    #achievement.register("DEEP_POCKETS")

    def can_unlock_achievement(name):
        global _enable_achievements
        if _enable_achievements and not achievement.has(name):
            return True
        else:
            return False
    
    def unlock_achievement(name):
        achievement.grant(name)
        achievement.sync()
        return

default _total_earned_gold = 0
default _total_cummed_characters = []
default _total_node_enter = 0
default _total_enemies_killed = 0
default _total_gold_spent_on_merchant = 0
