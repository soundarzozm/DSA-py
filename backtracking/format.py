def backtrack(variable):

    # Base Case
    if isSolved():
        # Save or Print ans

    # Solve for all choices
    for c in choices:

        # Control
        if isValid():

            # Update variable
            variable += change

            # Call itself
            backtack(variable)

            # Revert variable change
            variable -= change


if __name__ == "__main__":
    backtrack()
