"""
Helper module to expose all table models, the Base etc.
"""

# ====== import all tables here ======
from src.data_evaluation.db.base import Base
from src.data_evaluation.db.eval_conditions import EvalConditionTable
from src.data_evaluation.db.eval_msgs import EvalMsgTable
from src.data_evaluation.db.eval_results import EvalResultHistoryTable

# ====================================

ALL_TABLES: list[Base] = [EvalResultHistoryTable, EvalMsgTable, EvalConditionTable]
