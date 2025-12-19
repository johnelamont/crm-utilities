import time
import logging


def run_timer(seconds):
    """
    Run a timer for the specified number of seconds.

    Args:
        seconds (int): Number of seconds to wait

    Returns:
        dict: Response with status and message
    """
    logger = logging.getLogger()

    try:
        seconds = int(seconds)
        if seconds < 0:
            return {
                'status': 'error',
                'message': 'Seconds must be a positive number'
            }

        logger.info(f'Timer started for {seconds} seconds')
        time.sleep(seconds)
        logger.info(f'Timer completed after {seconds} seconds')

        return {
            'status': 'success',
            'message': f'Timer completed successfully after {seconds} seconds'
        }
    except ValueError:
        return {
            'status': 'error',
            'message': 'Invalid seconds parameter. Must be a valid integer.'
        }
    except Exception as e:
        logger.error(f'Error in run_timer: {str(e)}')
        return {
            'status': 'error',
            'message': f'An error occurred: {str(e)}'
        }
