import { json } from '@sveltejs/kit';

export async function POST({ locals: { supabase }, request, params }) {
	const { message } = await request.json();

	const { data, error } = await supabase
		.from('messages')
		.insert({
			type: message.type,
			content: message.content,
			chat_id: params.id
		})
		.select()
		.single();

	if (error) {
		return json(error, { status: 500 });
	}

	return json(data);
}
