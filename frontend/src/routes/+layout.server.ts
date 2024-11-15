export async function load({ locals: { safeGetSession }, cookies }) {
	const { session } = await safeGetSession();

	return { session, cookies: cookies.getAll() };
}
