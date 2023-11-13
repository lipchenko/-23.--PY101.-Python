disk_size = 1.44 * 1024 * 1024  # Размер дискеты в байтах
page_count = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4

# Вычисляем количество байт, требуемых для хранения одной книги
bytes_per_book = page_count * lines_per_page * chars_per_line * bytes_per_char

# Вычисляем количество книг, которые могут поместиться на дискету
books_on_disk = disk_size // bytes_per_book

print("Количество книг, которые можно поместить на дискету:", books_on_disk)
