
from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_demo_launch


def generate_launch_description():
    moveit_config = (
        MoveItConfigsBuilder("moveit_resources_fanuc")
        .robot_description(file_path="config/fanuc.urdf.xacro")
        .robot_description_semantic(file_path="config/fanuc.srdf")
        .trajectory_execution(file_path="config/moveit_controllers.yaml")
        .to_moveit_configs()
    )
    return generate_demo_launch(moveit_config)
