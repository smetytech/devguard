export async function signUp(email: string, password: string, name: string) {
	const url = '/api/auth/sign-up';
	const method = 'POST';
	const headers = { 'Content-Type': 'application/json' };
	const body = JSON.stringify({ email, password, name });

	const response = await fetch(url, { method, headers, body });
	const data = await response.json();

	if (!response.ok) {
		throw data;
	}
}

export async function signIn(email: string, password: string) {
	const url = '/api/auth/sign-in';
	const method = 'POST';
	const headers = { 'Content-Type': 'application/json' };
	const body = JSON.stringify({ email, password });

	const response = await fetch(url, { method, headers, body });
	const data = await response.json();

	if (!response.ok) {
		throw data;
	}
}

export async function signOut() {
	const url = '/api/auth/sign-out';
	const method = 'POST';
	const headers = { 'Content-Type': 'application/json' };

	const response = await fetch(url, { method, headers });
	const data = await response.json();

	if (!response.ok) {
		throw data;
	}
}

export async function resetPassword(password: string) {
	const url = '/api/auth/reset-password';
	const method = 'POST';
	const headers = { 'Content-Type': 'application/json' };
	const body = JSON.stringify({ password });

	const response = await fetch(url, { method, headers, body });
	const data = await response.json();

	if (!response.ok) {
		throw data;
	}
}

export async function sendPasswordResetEmail(email: string) {
	const url = '/api/auth/reset-password/request';
	const method = 'POST';
	const headers = { 'Content-Type': 'application/json' };
	const body = JSON.stringify({ email });

	const response = await fetch(url, { method, headers, body });
	const data = await response.json();

	if (!response.ok) {
		throw data;
	}
}
