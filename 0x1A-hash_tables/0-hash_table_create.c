#include "hash_tables.h"

/**
 * hash_table_create - hash_table_create
 * @size: size of array in hash table
 *
 * Return: hash table
 */
hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *ht = malloc(sizeof(hash_table_t));
	unsigned long int i = 0;

	if (ht == NULL)
		return (NULL);

	ht->size = size;
	ht->array = calloc(ht->size, sizeof(hash_node_t));

	if (ht->array == NULL)
		return (NULL);

	for (i = 0; i < size; i++)
		ht->array[i] = NULL;

	return (ht);
}
