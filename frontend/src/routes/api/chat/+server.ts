import { json } from '@sveltejs/kit';

export async function POST({ locals: { supabase,user } }) {
	
	const { data, error } = await supabase.from("chats").insert({
		user_id: user ? user.id : null,
	}).select().single();

	if (error) {
		
		return json(error, { status: 500 });
	}

	return json(data);
}