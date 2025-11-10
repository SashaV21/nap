import os
import subprocess
import sys
from behave import given, when, then

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
RESOURCES_DIR = os.path.join(PROJECT_ROOT, 'tests', 'resources')

@given('имеется тестовый файл "{filename}"')
def step_impl(context, filename):
    context.file_path = os.path.join(RESOURCES_DIR, filename)
    if not os.path.exists(context.file_path):
        raise FileNotFoundError(f"Тестовый файл не найден: {context.file_path}")

@when('я запускаю приложение с аргументами "{args}"')
def step_impl(context, args):
    arg_parts = args.split()
    # Подставляем полный путь, если файл из resources
    if hasattr(context, 'file_path'):
        arg_parts[0] = context.file_path

    cmd = [sys.executable, '-m', 'src.main'] + arg_parts
    result = subprocess.run(
        cmd,
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True
    )
    context.result = result

@then('вывод должен быть "{expected}"')
def step_impl(context, expected):
    assert context.result.returncode == 0, f"Ошибка: {context.result.stderr}"
    assert context.result.stdout.strip() == expected

@then('завершается с ошибкой')
def step_impl(context):
    assert context.result.returncode != 0