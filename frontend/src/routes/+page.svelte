<script lang="ts">
	import { onMount } from 'svelte';
	import {
		WebSocketMessageAction,
		type IWebSocketMessage
	} from '$lib/interfaces/websocket.interface';
	import { displayGeneralErrorToast } from '$lib/scripts/toast.script';
	import {
		closeWebSocket,
		openWebSocket,
		sendWebSocketMessage
	} from '$lib/scripts/websocket.script';

	let messages: Array<string> = $state([]);
	let value: string = $state('');

	function handleSubmit(event: Event) {
		event.preventDefault();

		if (!value.trim()) {
			return;
		}

		sendWebSocketMessage({ action: WebSocketMessageAction.SCAN, content: value });

		messages = [...messages, `> ${value}`];
		value = '';
	}

	function handleWebSocketMessage(message: IWebSocketMessage) {
		if (message.action === WebSocketMessageAction.SCAN) {
			messages = [...messages, `${message.content}`];
		}
	}

	function handleWebSocketError() {
		displayGeneralErrorToast();
	}

	onMount(() => {
		openWebSocket(handleWebSocketMessage, handleWebSocketError);

		return () => {
			closeWebSocket();
		};
	});
</script>

<div class="h-[calc(100dvh-4.5rem)] p-4 pt-0 lg:p-6 lg:pt-0">
	<div class="bg-muted flex h-full w-full flex-col rounded-xl font-mono">
		<div class="grow overflow-y-auto p-4">
			{#each messages as message}
				<p>{message}</p>
			{/each}
		</div>

		<form class="flex items-center gap-2" onsubmit={handleSubmit}>
			<div class="relative w-full">
				<span
					class="absolute left-4 top-1/2 flex w-4 -translate-y-1/2 items-center justify-center text-green-500"
				>
					$
				</span>

				<input
					class="placeholder:text-muted-foreground w-full border-none bg-transparent p-4 pl-10 outline-none"
					type="text"
					placeholder="Type a command..."
					bind:value
				/>
			</div>
		</form>
	</div>
</div>
