$(document).ready(function() {
    // Afficher le formulaire d'inscription
    $('#showSignup').click(function() {
        $('#formContainer').html(`
            <div class="card">
                <div class="card-body">
                    <h3 class="card-title">Sign Up</h3>
                    <form action="/signup" method="POST">
                        <div class="form-group">
                            <label for="signupUsername">Username</label>
                            <input type="text" class="form-control" id="signupUsername" name="username" required>
                        </div>
                        <div class="form-group">
                            <label for="signupEmail">Email</label>
                            <input type="email" class="form-control" id="signupEmail" name="email" required>
                        </div>
                        <div class="form-group">
                            <label for="signupPassword">Password</label>
                            <input type="password" class="form-control" id="signupPassword" name="password" required>
                        </div>
                        <div class="form-group">
                            <label for="signupRole">Role</label>
                            <select class="form-control" id="signupRole" name="role" required>
                                <option value="apprenant">Apprenant</option>
                                <option value="moniteur">Moniteur</option>
                                <option value="parent">Parent</option>
                            </select>
                        </div>
                        <button type="submit" class="btn btn-primary">Sign Up</button>
                    </form>
                </div>
            </div>
        `);
    });

    // Afficher le formulaire de connexion
    $('#showLogin').click(function() {
        $('#formContainer').html(`
            <div class="card">
                <div class="card-body">
                    <h3 class="card-title">Login</h3>
                    <form action="/login" method="POST">
                        <div class="form-group">
                            <label for="loginEmail">Email</label>
                            <input type="email" class="form-control" id="loginEmail" name="email" required>
                        </div>
                        <div class="form-group">
                            <label for="loginPassword">Password</label>
                            <input type="password" class="form-control" id="loginPassword" name="password" required>
                        </div>
                        <button type="submit" class="btn btn-primary">Login</button>
                    </form>
                </div>
            </div>
        `);
    });
});
