from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_move_group_launch


def generate_launch_description():
    moveit_config = (
        MoveItConfigsBuilder("moveit_resources_panda")
        .robot_description(file_path="config/panda.urdf.xacro")
        .robot_description_semantic(file_path="config/panda.srdf")
        .planning_pipelines(pipelines=["ompl", "chomp"])
        .trajectory_execution(file_path="config/gripper_moveit_controllers.yaml")
        .to_moveit_configs()
    )
    return generate_move_group_launch(moveit_config)
