# C - Hash tables

Searching could be a big problem when you working with a big data, fortunately the `Hash tables` making search like a peace of cake.

![](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnljOGJvd3hvMjJoeDhnZmkxemdxeHE1ejh3eTc5dzUwczdvcmdveSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JGBkyPlVQSsTJNgpG5/source.gif)

### Hash Tables - Magical Key-Value Storage ✨

Welcome to the enchanted world of Hash Tables! 🚀 These mystical functions allow you to conjure and manage your data like a wizard.

## Functions

### `hash_table_create`

```c
/**
 * hash_table_create - Creates a new Hash Table.
 * @size: The size of the array for the new hash table.
 *
 * Return: A pointer to the newly created hash table, or NULL if an error occurs.
 */
hash_table_t *hash_table_create(unsigned long int size);
```

Use this function to create a brand new Hash Table of magical proportions. Specify the size you desire, and it will be ready to store your secrets!

### `hash_djb2`

```c
/**
 * hash_djb2 - Hash function using the djb2 algorithm.
 * @str: The string to be hashed.
 *
 * Return: The hash value generated.
 */
unsigned long int hash_djb2(const unsigned char *str);
```

This function performs a magical hashing ritual on your strings using the `djb2` algorithm. It returns a unique hash value that will help us find the perfect spot in our mystical array.

### `key_index`

```c
/**
 * key_index - Finds the index of a key in the hash table.
 * @key: The key to search for.
 * @size: The size of the hash table array.
 *
 * Return: The index where the key should be stored in the array.
 */
unsigned long int key_index(const unsigned char *key, unsigned long int size);
```

Use this function to find the perfect index for your key in the array. It's like consulting a magical map to locate the treasure.

### `hash_table_set`

```c
/**
 * hash_table_set - Adds an element to the hash table.
 * @ht: The hash table to add the element to.
 * @key: The key for the new element.
 * @value: The value associated with the key.
 *
 * Return: 1 if successful, 0 otherwise.
 */
int hash_table_set(hash_table_t *ht, const char *key, const char *value);
```

This function lets you add a magical key-value pair to your hash table. It's like placing a new spell in your spellbook for future use.

### `hash_table_get`

```c
/**
 * hash_table_get - Retrieves the value associated with a key.
 * @ht: The hash table to search in.
 * @key: The key to search for.
 *
 * Return: The value associated with the key, or NULL if not found.
 */
char *hash_table_get(const hash_table_t *ht, const char *key);
```

Retrieve the value associated with a key from your spellbook (hash table). If the key is not found, fear not; the function returns NULL.

### `hash_table_print`

```c
/**
 * hash_table_print - Prints the contents of the hash table.
 * @ht: The hash table to print.
 */
void hash_table_print(const hash_table_t *ht);
```

This function prints the magical contents of your hash table. It's like opening your spellbook to share its secrets with the world.

### `hash_table_delete`

```c
/**
 * hash_table_delete - Deletes a hash table and its elements.
 * @ht: The hash table to delete.
 */
void hash_table_delete(hash_table_t *ht);
```

Use this function when it's time to clean up and close your spellbook. It deletes the entire hash table and frees the magic within.
