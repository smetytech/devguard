<script lang="ts">
	import { onMount } from 'svelte';
	import type { IWebSocketMessage } from '$lib/interfaces/websocket.interface';
	import { displayGeneralErrorToast } from '$lib/scripts/toast.script';
	import { closeWebSocket, openWebSocket } from '$lib/scripts/websocket.script';

	function handleWebSocketMessage(message: IWebSocketMessage) {
		console.log(message);
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
