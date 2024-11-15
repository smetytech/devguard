<script lang="ts">
	import { marked } from 'marked';
	import { MessageType, type IMessage } from '$lib/interfaces/message.interface';

	export let message: IMessage;
</script>

<div class="flex items-start gap-2">
	<span
		class="{message.type === MessageType.User
			? 'text-green-500'
			: 'text-muted-foreground'} shrink-0 text-sm leading-6"
	>
		~{message.name} %
	</span>

	<div class="prose dark:prose-invert">
		{@html marked.parse(message.content)}
	</div>

	<span class="text-muted-foreground ml-auto text-sm leading-6">{message.timestamp}</span>
</div>
