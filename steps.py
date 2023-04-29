"""
Note: No output is returned when passed(), failed(), or errored() is called
"""

from typing import Any, Union, Dict, List, Tuple

def error_to_string(e) -> str:
    """
    Converts an error into an informational string format.
    Used in ParentTest.start_step() and ParentTest.troubleshootable_step()
    """
    return f"{type(e).__name__}: {', '.join(e.args)}"

class Steps:
    @classmethod
    def set_steps(cls, steps):
        cls.steps = steps
    
    @classmethod
    def set_log(cls, log):
        cls.log = log

    @classmethod
    def passed(cls, explanation: str):
        cls.step_passed = True

        if cls.step is not None:
            step = cls.step
            cls.step=None
            step.passed(explanation)
            return True

        else:
            cls.log.info(explanation)
            return True

    @classmethod
    def skipped(cls, explanation: str):
        cls.step_passed = True

        if cls.step is not None:
            step = cls.step
            cls.step=None
            step.skipped(explanation)
            return True

        else:
            cls.log.info(explanation)
            return True

    @classmethod
    def passx(cls, explanation: str):
        cls.step_passed = True

        if cls.step is not None:
            step = cls.step
            cls.step=None
            step.passx(explanation)
            return True

        else:
            cls.log.info(explanation)
            return True

    @classmethod
    def failed(cls, explanation: str):
        cls.step_passed = False

        if cls.step is not None:
            step = cls.step
            cls.step=None
            step.failed(explanation)
            return False
        
        else:
            cls.log.warning(explanation)
            return False

    @classmethod
    def error(cls, explanation: str):
        cls.step_passed = False

        if cls.step is not None:
            step = cls.step
            cls.step=None
            step.failed(explanation)
            return False
        
        else:
            cls.log.error(explanation)
            return False

    @classmethod
    def start(cls, step_txt: str, continue_: bool = False) -> Any: 
        """
        First Set of Parameters
        -----------------------
        step_txt: str
            The name of the step.

        continue_: bool (Default: False)
            Whether to move on to the next step after this step and any potential troubleshoot are complete.

        Second Set of Parameters
        ------------------------
        step_function: callable
            Which function to execute in this step.
            This function will accept all the arguments in the third set of parameters.
        
        troubleshoot_function: callable (Default: None)
            Which function to execute if the step_function failed.
            If none is given, do not perform troubleshooting.
            this function will accept the step_function's output, as well as all the arguments in the third set of parameters.
        
        Third Set of Parameters
        -----------------------
        *args: any positional arguments
            The positional arguments to use in step_function and troubleshoot_function.
        
        **kwargs: any keyword=value declaration
            The named arguments to use in step_function and troubleshoot_function.

        
        Output
        ------
        Anything returned by the inner function

        Usage
        -----
        Steps.start(step_txt="step description", continue_=True) \\\n
            (step_function, troubleshoot_function)(step_parameters)
        
        Note
        ----
        To fail the function, use Steps.failed()
        """
        cls.step_txt = step_txt
        cls.step_passed = True
        cls.output = None

        def inner(step_function: callable, troubleshoot_function: callable=None):
            def wrapper(*args, **kwargs):
                step_continue_ = continue_ or troubleshoot_function is not None
                with cls.steps.start(step_txt, continue_=step_continue_) as step:
                    cls.step = step
                    try:
                        cls.output = step_function(*args, **kwargs)
                        cls.step = None
                    except Exception as e:
                        fail_message = error_to_string(e)
                        cls.error(fail_message)
                
                if not cls.step_passed and troubleshoot_function is not None:
                    with cls.steps.start(f"Troubleshoot {step_txt}", continue_=continue_) as step:
                        cls.step = step
                        try:
                            troubleshoot_output = troubleshoot_function(cls.output, *args, **kwargs)
                            cls.step = None
                            step.failed("Troubleshoot complete")
                        except Exception as e:
                            fail_message = error_to_string(e)
                            cls.error(fail_message)
                return cls.output
            return wrapper
        return inner
