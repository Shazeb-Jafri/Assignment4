from Crud import create_or_update_entry, delete_entry, display_data

def main():
    print("\nCRUD Operations:")
    while True:
        print("1. Read")
        print("2. Create/Update")
        print("3. Delete")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_data()
        elif choice == '2':
            item_id = int(input("Enter the item ID to create/update: "))
            new_item = {
                "id": item_id,
                "Title": input("Enter the title: "),
                "Publisher": input("Enter the publisher: "),
                "Release Date": input("Enter the release date: "),
                "Author": input("Enter the author: ")
            }
            create_or_update_entry(item_id, new_item)
        elif choice == '3':
            item_id = int(input("Enter the item ID to delete: "))
            delete_entry(item_id)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1-4.")

if __name__ == '__main__':
    main()

