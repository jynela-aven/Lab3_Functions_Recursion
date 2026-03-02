CONTROL_NUM = 14
FAVORITE_ARTIST = "RUEL"
artist_length = len(FAVORITE_ARTIST)


final_decision = "authorize"(CONTROL_NUM, artist_length)
print(f"Final Authorization Decision: {final_decision}")

initial_power = CONTROL_NUM * artist_length
total_recursive_calls = "signal_shutdown"(initial_power)
print(f"Total Recursive Calls: {total_recursive_calls}")

stream_limit = CONTROL_NUM * artist_length
play_counts = list("play_count_stream"(stream_limit))
total_plays = sum(play_counts)
num_records = len(play_counts)

print("\n=== Assessment Data ===")
print(f"CONTROL NUM Used: {CONTROL_NUM}")
print(f"FAVORITE ARTIST Used: {FAVORITE_ARTIST}")
print(f"Computed Stream Limit: {stream_limit}")
print(f"Generated Play Counts: {play_counts}")
print(f"Total Plays: {total_plays}")
print(f"Number of Records Processed: {num_records}")
print(f"Total Recursive Calls (Signal Shutdown): {total_recursive_calls}")
