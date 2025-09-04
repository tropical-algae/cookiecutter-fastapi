from pydantic_settings import BaseSettings


class Constant(BaseSettings):
    # 返回值
    RESP_200: str = "success"
    RESP_VALIDATION_ERROR: str = "参数校验错误"
    RESP_SERVER_ERROR: str = "服务器错误"
    TOKEN_NOT_MATCH: str = "Token校验失败"
    # 权限
    ROLE_ADMIN_DESCRIPTION: str = "系统管理员，管理所有数据"
    ROLE_USER_DESCRIPTION: str = "系统用户，查看自己用户数据"
    ROLE_GUEST_DESCRIPTION: str = "访客，查看公开数据"
    # 用户
    USER_NOT_ENOUGH_PERMISSION: str = "当前用户权限不足"
    USER_NOT_ACTIVE: str = "当前账户已暂停使用"
    USER_INCORRECT_PASSWORD: str = "用户名或密码错误"
    USER_EXISTS: str = "用户名已存在"
    USER_NOT_EXISTS: str = "用户不存在"
    # task 任务
    INFERENCE_RESULT_NOT_EXISTS: str = "推理结果不存在"
    DELETE_INFERENCE_RESULT_FILE_FAIL: str = "删除推理结果文件失败"


CONSTANT = Constant()
