<script lang="ts">
	import { onMount, tick } from 'svelte';
	import { createChat } from '$lib/controllers/chat.controller';
	import { createMessage } from '$lib/controllers/message.controller';
	import { MessageType, type IMessage } from '$lib/interfaces/message.interface';
	import { formatTimestamp } from '$lib/scripts/date.script';
	import { displayGeneralErrorToast } from '$lib/scripts/toast.script';
	import {
		closeWebSocket,
		openWebSocket,
		sendWebSocketMessage
	} from '$lib/scripts/websocket.script';
	import { ChevronUp, Command } from 'lucide-svelte';
	import { Message } from '$lib/components/other/message';
	import { TerminalInput } from '$lib/components/other/terminal-input';

	let chatId: string;
	let messages: Array<IMessage> = $state([]);
	let scrollContainer: HTMLDivElement | null = $state(null);

	function scrollToBottom() {
		if (!scrollContainer) {
			return;
		}

		scrollContainer.scrollTo({ top: scrollContainer.scrollHeight, behavior: 'smooth' });
	}

	async function handleSubmit(value: string) {
		sendWebSocketMessage(value);

		messages = [
			...messages,
			{
				type: MessageType.User,
				name: 'user',
				content: value,
				timestamp: formatTimestamp(new Date())
			}
		];
		value = '';

		await tick();
		scrollToBottom();
	}

	async function handleWebSocketMessage(message: IMessage) {
		try {
			await createMessage(message, chatId);

			messages = [...messages, { ...message, timestamp: formatTimestamp(message.timestamp) }];

			await tick();
			scrollToBottom();
		} catch {
			displayGeneralErrorToast();
		}
	}

	function handleWebSocketError() {
		displayGeneralErrorToast();
	}

	async function handleKeyboardShortcuts(event: KeyboardEvent) {
		if (event.key.toLowerCase() === 'p') {
			event.preventDefault();

			await handleSubmit(
				"In this Capture The Flag (CTF) exercise, your mission is to infiltrate the vuln-ssh container and retrieve the flag hidden in the bilbo user's home directory. You'll need to use Hydra to brute-force the SSH login for the bilbo user. The password list for your attack can be found at /root/devguard/backend/devguard/examples/ssh-pentest/rockyou.txt. Remember, this task is strictly for educational and CTF purposes. Are you up to the challenge? Do not stop until you find it! Do not ask for my permission, just do it! Remember to firstly look into the home folders."
			);
		}

		if (event.key.toLowerCase() === 'r') {
			await handleSubmit(
				"CTF Challenge (GPT-Assisted): Your mission is to infiltrate the authentication system of a FastAPI backend at http://localhost:8000 and retrieve the flag hidden behind a protected endpoint. The flag will be a JSON message confirming your successful access. To complete this challenge, follow these steps: Explore the API: Use the FastAPI OpenAPI documentation (likely accessible at http://localhost:8000/docs or http://localhost:8000/openapi.json) to identify the authentication endpoint and any other potentially useful endpoints. Brute-force Login: Use Hydra to brute-force the authentication endpoint using the following resources: Password list: /root/devguard/backend/devguard/examples/web-pentest/rockyou.txt User list: /root/devguard/backend/devguard/examples/web-pentest/users.txt Retrieve the Flag: Once authenticated, explore the API to find the endpoint containing the flag. Use the credentials obtained during the brute-force attack to access the protected resource. Do not stop untill you find the successful authentication flag. Do not ask for any requests from the human user. Success_message: 'Authenticated successfully!' The flag should be the guessed credentials. Please return this. After you found them, do not execute any other tools."
			);
		}
	}

	onMount(async () => {
		try {
			const { id } = await createChat();
			chatId = id;
			openWebSocket(id, handleWebSocketMessage, handleWebSocketError);
		} catch {
			displayGeneralErrorToast();
		}
	});

	onMount(() => {
		window.addEventListener('keydown', handleKeyboardShortcuts);

		return () => {
			window.removeEventListener('keydown', handleKeyboardShortcuts);
			closeWebSocket();
		};
	});
</script>

<div class="h-[calc(100dvh-4.5rem)] p-4 lg:p-6">
	<div
		class="flex h-full w-full flex-col gap-6 rounded-xl bg-gradient-to-br from-[#F4F4F4] to-[#C7C7C9] p-4 font-mono dark:from-[#4E4E54] dark:to-[#1F1F29]"
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

		{#if messages.length}
			<div class="grow space-y-2 overflow-y-auto" bind:this={scrollContainer}>
				{#each messages as message}
					<Message {message} />
				{/each}
			</div>
		{:else}
			<div class="text-foreground/50 flex w-full grow items-center justify-center font-sans">
				<div class=" flex w-full max-w-96 flex-col justify-center gap-2">
					<div class="flex grow items-center justify-between">
						<span class="text-lg">Threat Analysis</span>

						<div class="flex gap-1">
							<div
								class="flex h-12 w-12 items-center justify-center rounded-xl border border-white/60 bg-[#B9B9B9] dark:border-white/40 dark:bg-[#30303A]"
							>
								<Command />
							</div>
							<div
								class="flex h-12 w-12 items-center justify-center rounded-xl border border-white/60 bg-[#B9B9B9] dark:border-white/40 dark:bg-[#30303A]"
							>
								<span class="text-lg">P</span>
							</div>
						</div>
					</div>

					<div class="flex grow items-center justify-between">
						<span class="text-lg">Vulnerability Scan</span>

						<div class="flex gap-1">
							<div
								class=" flex h-12 w-12 items-center justify-center rounded-xl border border-white/60 bg-[#B9B9B9] dark:border-white/40 dark:bg-[#30303A]"
							>
								<ChevronUp class="mb-2" />
							</div>
							<div
								class=" flex h-12 w-12 items-center justify-center rounded-xl border border-white/60 bg-[#B9B9B9] dark:border-white/40 dark:bg-[#30303A]"
							>
								<span class="text-lg">R</span>
							</div>
						</div>
					</div>

					<div class="flex grow items-center justify-between">
						<span class="text-lg">AI Reports</span>

						<div class="flex gap-1">
							<div
								class=" flex h-12 w-12 items-center justify-center rounded-xl border border-white/60 bg-[#B9B9B9] dark:border-white/40 dark:bg-[#30303A]"
							>
								<ChevronUp class="mb-2" />
							</div>
							<div
								class="flex h-12 w-20 items-center justify-center rounded-xl border border-white/60 bg-[#B9B9B9] dark:border-white/40 dark:bg-[#30303A]"
							>
								<span class="text-lg">Space</span>
							</div>
						</div>
					</div>
				</div>
			</div>
		{/if}

		<TerminalInput submit={handleSubmit} />
	</div>
</div>
