def distribute_artifacts_and_bonuses(
    budget, num_packages, num_curators, package_weights
):
    # Sort package weights for easier grouping with minimized weight differences
    package_weights.sort()

    # Distribute packages as evenly as possible to minimize weight differences
    groups = [[] for _ in range(num_curators)]
    for i, weight in enumerate(package_weights):
        groups[i % num_curators].append(weight)

    # Calculate total weight per curator group
    total_weights = [sum(group) for group in groups]

    # Calculate bonuses based on total weight handled
    max_bonus_pool = 0.15 * budget  # 15% of budget
    total_weight_handled = sum(total_weights)
    bonuses = [
        (weight / total_weight_handled) * max_bonus_pool for weight in total_weights
    ]

    # Display the result
    for i, (group, bonus) in enumerate(zip(groups, bonuses), 1):
        print(f"Curator {i}: Artifact weights = {group}, Bonus = ${bonus:.2f}")


# Test case
budget = 10000
num_packages = 6
num_curators = 3
package_weights = [25.5, 32.0, 28.5, 40.0, 35.5, 30.0]

distribute_artifacts_and_bonuses(budget, num_packages, num_curators, package_weights)
