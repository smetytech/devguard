export function validateEmail(email: string) {
	return /^[\w.-]+@[\w.-]+\.\w+$/.test(email);
}

export function validatePassword(password: string) {
	if (password.length < 8) {
		return false;
	}

	const hasLowercase = /[a-z]/.test(password);
	const hasUppercase = /[A-Z]/.test(password);
	const hasDigit = /\d/.test(password);
	const hasSpecialChar = /[\W_]/.test(password);

	return hasLowercase && hasUppercase && hasDigit && hasSpecialChar;
}
