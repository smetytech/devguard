import { json } from '@sveltejs/kit';

export async function POST({ locals: { supabase }, request, params }) {
	const { type, content } = await request.json();
	const { data, error } = await supabase.from("messages").insert({
		chat_id: params.id, type, content
	}).select().single();

	if (error) {

		return json(error, { status: 500 });
	}

	return json(data);
}