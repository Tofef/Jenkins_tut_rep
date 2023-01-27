# Protocol Constants

CMD_FIELD_LENGTH = 16	# Exact length of cmd field (in bytes)
LENGTH_FIELD_LENGTH = 4   # Exact length of length field (in bytes)
MAX_DATA_LENGTH = 10**LENGTH_FIELD_LENGTH-1  # Max size of data field according to protocol
MSG_HEADER_LENGTH = CMD_FIELD_LENGTH + 1 + LENGTH_FIELD_LENGTH + 1  # Exact size of header (CMD+LENGTH fields)
MAX_MSG_LENGTH = MSG_HEADER_LENGTH + MAX_DATA_LENGTH  # Max size of total message
DELIMITER = "|"  # Delimiter character in protocol
DATA_DELIMITER = "#"  # Delimiter in the data part of the message

# Protocol Messages 
# In this dictionary we will have all the client and server command names

PROTOCOL_CLIENT = {
"login_msg" : "LOGIN",
"logout_msg" : "LOGOUT"
} # .. Add more commands if needed


PROTOCOL_SERVER = {
"login_ok_msg" : "LOGIN_OK",
"login_failed_msg" : "ERROR"
} # ..  Add more commands if needed


# Other constants

ERROR_RETURN = None  # What is returned in case of an error

def split_data(msg, expected_fields):
	"""
	Helper method. gets a string and number of expected fields in it. Splits the string 
	using protocol's data field delimiter (|#) and validates that there are correct number of fields.
	Returns: list of fields if all ok. If some error occured, returns None
	"""
	# A reference to edge cases should be added

	if (msg.count(DATA_DELIMITER) == expected_fields):
		return(msg.split(DATA_DELIMITER))
	else:
		return([None])


def join_data(msg_fields):
	"""
	Helper method. Gets a list, joins all of it's fields to one string divided by the data delimiter. 
	Returns: string that looks like cell1#cell2#cell3
	"""
	return (DATA_DELIMITER.join(str(item) for item in msg_fields))


def build_message(cmd, data):
	"""
	Gets command name (str) and data field (str) and creates a valid protocol message
	Returns: str, or None if error occured
	"""

	full_msg = ''

	if (cmd=='LOGIN'):
		full_msg = cmd.ljust(16) + DELIMITER + (str(len(data))).zfill(4) + DELIMITER + data
	elif (cmd=='LOGOUT'):
		full_msg = cmd.ljust(16) + DELIMITER + (str('0')).zfill(4) + DELIMITER 
	elif (cmd=='LOGGED'):
		full_msg = cmd.ljust(16) + DELIMITER + (str('0')).zfill(4) + DELIMITER 
	elif (cmd=='GET_QUESTION'):
		full_msg = cmd.ljust(16) + DELIMITER + (str('0')).zfill(4) + DELIMITER 
	elif (cmd=='SEND_ANSWER'):
		full_msg = cmd.ljust(16) + DELIMITER + (str(len(data))).zfill(4) + DELIMITER + data
	elif (cmd=='MY_SCORE'):
		full_msg = cmd.ljust(16) + DELIMITER + (str('0')).zfill(4) + DELIMITER 
	elif (cmd=='HIGHSCORE'):
		full_msg = cmd.ljust(16) + DELIMITER + (str('0')).zfill(4) + DELIMITER 
	elif (cmd=='LOGIN_OK'):
		full_msg = cmd.ljust(16) + DELIMITER + (str('0')).zfill(4) + DELIMITER 
	elif (cmd=='LOGGED_ANSWER'):
		full_msg = cmd.ljust(16) + DELIMITER + (str(len(data))).zfill(4) + DELIMITER + data
	elif (cmd=='YOUR_QUESTION'):
		full_msg = cmd.ljust(16) + DELIMITER + (str(len(data))).zfill(4) + DELIMITER + data
	elif (cmd=='CORRECT_ANSWER'):
		full_msg = cmd.ljust(16) + DELIMITER + (str('0')).zfill(4) + DELIMITER 
	elif (cmd=='WRONG_ANSWER'):
		full_msg = cmd.ljust(16) + DELIMITER + (str(len(data))).zfill(4) + DELIMITER + data
	elif (cmd=='YOUR_SCORE'):
		full_msg = cmd.ljust(16) + DELIMITER + (str(len(data))).zfill(4) + DELIMITER + data
	elif (cmd=='ALL_SCORE'):
		full_msg = cmd.ljust(16) + DELIMITER + (str(len(data))).zfill(4) + DELIMITER + data
	elif (cmd=='ERROR'):
		full_msg = cmd.ljust(16) + DELIMITER + (str(len(data))).zfill(4) + DELIMITER + data
	elif (cmd=='NO_QUESTIONS'):
		full_msg = cmd.ljust(16) + DELIMITER + (str('0')).zfill(4) + DELIMITER 
	else:
		return None
	
	return full_msg


def parse_message(data):
	"""
	Parses protocol message and returns command name and data field
	Returns: cmd (str), data (str). If some error occured, returns None, None
	"""
	splitted_data = data.split(DELIMITER)
	cmd = splitted_data[0].replace(" ", "")
	msg_len = int(splitted_data[1])
	msg = splitted_data[2]
	if (len(msg) != msg_len):
		cmd = None
		msg = None
	return cmd, msg

	

