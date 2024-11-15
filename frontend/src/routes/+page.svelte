<script lang="ts">
	import { onMount } from 'svelte';
	import { MessageType, type IMessage } from '$lib/interfaces/message.interface';
	import { displayGeneralErrorToast } from '$lib/scripts/toast.script';
	import {
		closeWebSocket,
		openWebSocket,
		sendWebSocketMessage
	} from '$lib/scripts/websocket.script';
	import { formatTimestamp } from '$lib/scripts/date.script';
	import { CornerDownLeft } from 'lucide-svelte';

	let messages: Array<IMessage> = $state([]);
	let value: string = $state('');

	function handleSubmit(event: Event) {
		event.preventDefault();

		if (!value.trim()) {
			return;
		}

		sendWebSocketMessage(value);

		messages = [
			...messages,
			{
				type: MessageType.User,
				name: 'User',
				content: value,
				timestamp: formatTimestamp(new Date())
			},
			{
				type: MessageType.Tool,
				name: 'DevGuard Agent',
				content: value,
				timestamp: formatTimestamp(new Date())
			}
		];
		value = '';
	}

	function handleWebSocketMessage(message: IMessage) {
		messages = [...messages, { ...message, timestamp: formatTimestamp(message.timestamp) }];
	}

	function handleWebSocketError() {
		// displayGeneralErrorToast();
	}

	onMount(() => {
		openWebSocket(handleWebSocketMessage, handleWebSocketError);

		return () => {
			closeWebSocket();
		};
	});
</script>

<div class="h-[calc(100dvh-4.5rem)] p-4 lg:p-6">
	<div
		class="flex h-full w-full flex-col gap-4 rounded-xl bg-gradient-to-br from-[#F4F4F4] to-[#C7C7C9] p-4 font-mono dark:from-[#64636B] dark:to-[#1F1F29]"
	>
		<div class="flex items-center justify-center">
			<div class="flex items-center gap-1.5">
				<span class="h-3.5 w-3.5 rounded-full bg-[#ED6A5E]"></span>
				<span class="h-3.5 w-3.5 rounded-full bg-[#F4BF4F]"></span>
				<span class="h-3.5 w-3.5 rounded-full bg-[#61C554]"></span>
			</div>

			<span class="mx-auto block w-fit text-center text-sm">Terminal</span>

			<div class="flex items-center gap-1.5 opacity-0">
				<span class="h-3.5 w-3.5 rounded-full bg-[#ED6A5E]"></span>
				<span class="h-3.5 w-3.5 rounded-full bg-[#F4BF4F]"></span>
				<span class="h-3.5 w-3.5 rounded-full bg-[#61C554]"></span>
			</div>
		</div>

		<div class="grow space-y-1 overflow-y-auto">
			{#each messages as message}
				{#if message.type === MessageType.User}
					<div class="flex items-center gap-2.5 p-4">
						<span class="text-muted-foreground text-sm">{message.timestamp}</span>
						<span class="font-medium">{message.content}</span>
					</div>
				{:else}
					<div class="flex items-center gap-2.5">
						<span class="text-muted-foreground text-sm opacity-0">{message.timestamp}</span>

						<div class="bg-background/40 dark:bg-background/25 grow rounded-xl p-4">
							<span class="text-muted-foreground block text-xs">{message.name}</span>
							<span class="block">{message.content}</span>
						</div>
					</div>
				{/if}
			{/each}
		</div>

		<form class="bg-muted/75 flex items-center gap-2 rounded-xl pl-4" onsubmit={handleSubmit}>
			<span class="text-green-500">~user</span>

			<input
				class="placeholder:text-muted-foreground grow border-none bg-transparent py-4 outline-none"
				type="text"
				bind:value
			/>

			<div class="pr-4">
				<CornerDownLeft />
			</div>
		</form>
	</div>
</div>
